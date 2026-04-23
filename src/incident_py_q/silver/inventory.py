"""Silver-path inventory extraction and loading for HAR-derived SDK methods."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from collections.abc import Collection, Mapping, Sequence
from dataclasses import asdict, dataclass
from importlib.resources import files
from pathlib import Path
from typing import Any, Literal, cast
from urllib.parse import parse_qsl, urlparse

from incident_py_q._utils import to_snake_case
from incident_py_q.apps import build_app_method_metadata
from incident_py_q.schema.registry import SchemaRegistry

SilverParameterLocation = Literal["path", "query", "body", "file"]
JSONPayload = dict[str, Any] | list[Any] | None

_UUID_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
    re.IGNORECASE,
)
_INT_RE = re.compile(r"^\d+$")
_BOOL_RE = re.compile(r"^(true|false)$", re.IGNORECASE)
_STATIC_SUFFIXES = (
    ".css",
    ".gif",
    ".html",
    ".ico",
    ".jpeg",
    ".jpg",
    ".js",
    ".png",
    ".svg",
    ".web.html",
)
_DISCARD_EXACT = {
    "/",
    "/%7B%7B%20$ctrl.IconUri%20%7D%7D",
    "/css",
    "/favicon-32x32.png",
    "/favicon.ico",
    "/manifest.json",
    "/robots.txt",
}
_DISCARD_PREFIXES = (
    "/core/",
    "/helpcenter/",
    "/img/",
    "/media/",
    "/pub/",
    "/rte/",
    "/v2/track",
    "/webpacks/",
)
_NOISY_METHOD_TOKENS = {"api", "app", "data"}
_MANUAL_APP_ROUTE_PREFIXES = ("/apps/", "/api/v1.0/apps/", "/api/v1.0/app-registry/")
_SUPPRESSED_SILVER_ROUTES = {
    ("POST", "/profiles/my/picture"),
}
_PARAMETER_HINTS = {
    "app",
    "asset",
    "audit",
    "category",
    "entity",
    "file",
    "filter",
    "job",
    "key",
    "model",
    "permission",
    "policy",
    "requestor",
    "resolution",
    "rule",
    "serial",
    "set",
    "site",
    "status",
    "subtask",
    "survey",
    "team",
    "ticket",
    "type",
    "user",
    "view",
    "widget",
}


@dataclass(slots=True, frozen=True)
class SilverParameterMetadata:
    """One inferred Silver-path parameter."""

    python_name: str
    api_name: str
    location: SilverParameterLocation
    required: bool
    type_display: str
    description: str


@dataclass(slots=True, frozen=True)
class SilverMethodMetadata:
    """One HAR-derived undocumented SDK method."""

    namespace_path: tuple[str, ...]
    method_name: str
    http_method: str
    route: str
    parameters: tuple[SilverParameterMetadata, ...]
    summary: str
    description: str
    typed_return: str
    raw_return: str
    sources: tuple[str, ...]
    status_codes: tuple[int, ...]
    uses_app_headers: bool

    @property
    def namespace(self) -> str:
        """Return the dot-qualified namespace path without the Silver root."""
        return ".".join(self.namespace_path)


@dataclass(slots=True)
class _ObservedRequest:
    method: str
    raw_path: str
    normalized_path: str
    source: str
    status_code: int | None
    query: dict[str, str]
    file_fields: tuple[str, ...]
    body: Any | None


@dataclass(slots=True)
class _Aggregate:
    method: str
    route: str
    normalized_route: str
    namespace_path: tuple[str, ...]
    method_name: str
    uses_app_headers: bool
    parameters: list[SilverParameterMetadata]
    sources: set[str]
    status_codes: set[int]


def load_silver_inventory() -> tuple[SilverMethodMetadata, ...]:
    """Load the checked-in Silver inventory bundled with the package."""
    path = files("incident_py_q").joinpath("data/silver_inventory.json")
    payload = json.loads(path.read_text(encoding="utf-8"))
    endpoints = payload.get("endpoints", [])
    if not isinstance(endpoints, list):
        raise ValueError("Bundled silver_inventory.json must contain an 'endpoints' list.")
    loaded: list[SilverMethodMetadata] = []
    for endpoint in endpoints:
        if not isinstance(endpoint, dict):
            continue
        raw_parameters = endpoint.get("parameters", [])
        parameters = tuple(
            SilverParameterMetadata(
                python_name=str(parameter["python_name"]),
                api_name=str(parameter["api_name"]),
                location=cast(SilverParameterLocation, str(parameter["location"])),
                required=bool(parameter["required"]),
                type_display=str(parameter["type_display"]),
                description=str(parameter["description"]),
            )
            for parameter in raw_parameters
            if isinstance(parameter, dict)
        )
        loaded.append(
            SilverMethodMetadata(
                namespace_path=tuple(str(part) for part in endpoint["namespace_path"]),
                method_name=str(endpoint["method_name"]),
                http_method=str(endpoint["http_method"]),
                route=str(endpoint["route"]),
                parameters=parameters,
                summary=str(endpoint["summary"]),
                description=str(endpoint["description"]),
                typed_return=str(endpoint["typed_return"]),
                raw_return=str(endpoint["raw_return"]),
                sources=tuple(sorted(str(source) for source in endpoint.get("sources", []))),
                status_codes=tuple(sorted(int(code) for code in endpoint.get("status_codes", []))),
                uses_app_headers=bool(endpoint.get("uses_app_headers", False)),
            )
        )
    return tuple(sorted(loaded, key=lambda item: (item.namespace_path, item.method_name)))


def extract_silver_inventory(
    *,
    har_files: Sequence[str | Path],
    registry: SchemaRegistry,
) -> tuple[SilverMethodMetadata, ...]:
    """Build canonical Silver metadata from one or more HAR files."""
    observed = _load_observed_requests(har_files=har_files, registry=registry)
    variable_positions = _build_variable_position_map(observed)
    aggregates: dict[tuple[str, str], _Aggregate] = {}
    manual_routes = _manual_app_routes()

    for item in observed:
        raw_template = _template_raw_path(item.raw_path, item.normalized_path, variable_positions)
        if (item.method, _route_shape(raw_template)) in manual_routes:
            continue
        normalized_template = _normalize_for_matching(raw_template)
        key = (item.method, raw_template)
        aggregate = aggregates.get(key)
        if aggregate is None:
            namespace_path = _namespace_path_from_normalized(normalized_template)
            method_name = _build_method_name(
                http_method=item.method,
                namespace_path=namespace_path,
                normalized_route=normalized_template,
            )
            path_parameters = _build_path_parameters(
                route=raw_template,
                normalized_route=normalized_template,
                observed_items=[candidate for candidate in observed if candidate.method == item.method],
            )
            aggregate = _Aggregate(
                method=item.method,
                route=raw_template,
                normalized_route=normalized_template,
                namespace_path=namespace_path,
                method_name=method_name,
                uses_app_headers=_uses_app_headers(raw_template),
                parameters=path_parameters,
                sources=set(),
                status_codes=set(),
            )
            aggregates[key] = aggregate

        aggregate.sources.add(item.source)
        if item.status_code is not None:
            aggregate.status_codes.add(item.status_code)

    for aggregate in aggregates.values():
        matching_items = [
            item
            for item in observed
            if item.method == aggregate.method
            and _template_raw_path(item.raw_path, item.normalized_path, variable_positions) == aggregate.route
        ]
        aggregate.parameters.extend(_build_query_parameters(matching_items))
        aggregate.parameters.extend(_build_file_parameters(matching_items))
        aggregate.parameters.extend(_build_body_parameters(matching_items))

    extracted = [
        SilverMethodMetadata(
            namespace_path=aggregate.namespace_path,
            method_name=aggregate.method_name,
            http_method=aggregate.method,
            route=aggregate.route,
            parameters=tuple(aggregate.parameters),
            summary=_build_summary(aggregate),
            description=_build_description(aggregate),
            typed_return="dict[str, Any] | list[Any] | None",
            raw_return="dict[str, Any] | list[Any] | None",
            sources=tuple(sorted(aggregate.sources)),
            status_codes=tuple(sorted(aggregate.status_codes)),
            uses_app_headers=aggregate.uses_app_headers,
        )
        for aggregate in aggregates.values()
    ]

    if not any(
        endpoint.http_method == "GET" and endpoint.route == "/assets/serial/{serial}"
        for endpoint in extracted
    ):
        extracted.append(
            SilverMethodMetadata(
                namespace_path=("assets",),
                method_name="get_asset_by_serial",
                http_method="GET",
                route="/assets/serial/{serial}",
                parameters=(
                    SilverParameterMetadata(
                        python_name="serial",
                        api_name="serial",
                        location="path",
                        required=True,
                        type_display="str",
                        description=(
                            "Serial number path segment. This Silver route is added explicitly "
                            "because it is known to exist even when the HAR does not capture it."
                        ),
                    ),
                ),
                summary="Silver path for asset lookup by serial number.",
                description=(
                    "This route is treated as Silver because bundled Stoplight contracts do not "
                    "define it. The SDK exposes it separately so Golden Stoplight methods remain "
                    "the authoritative contract whenever they exist."
                ),
                typed_return="dict[str, Any] | list[Any] | None",
                raw_return="dict[str, Any] | list[Any] | None",
                sources=("synthetic_required_route",),
                status_codes=(),
                uses_app_headers=False,
            )
        )

    return tuple(sorted(_dedupe_method_names(extracted), key=lambda item: (item.namespace_path, item.method_name)))


def silver_inventory_payload(metadata: Sequence[SilverMethodMetadata]) -> dict[str, Any]:
    """Serialize Silver metadata for the checked-in JSON artifact."""
    return {
        "endpoints": [
            {
                **asdict(endpoint),
                "namespace_path": list(endpoint.namespace_path),
                "sources": list(endpoint.sources),
                "status_codes": list(endpoint.status_codes),
                "parameters": [asdict(parameter) for parameter in endpoint.parameters],
            }
            for endpoint in metadata
        ]
    }


def silver_inventory_records(metadata: Sequence[SilverMethodMetadata]) -> list[dict[str, Any]]:
    """Return a stable JSON-serializable contract inventory for Silver methods."""
    return [
        {
            "provenance": "silver",
            "namespace": method.namespace,
            "name": method.method_name,
            "http_method": method.http_method,
            "path": method.route,
            "sources": list(method.sources),
        }
        for method in sorted(metadata, key=lambda item: (item.namespace_path, item.method_name))
    ]


def legacy_app_inventory_records(metadata: Sequence[SilverMethodMetadata]) -> list[dict[str, Any]]:
    """Return the legacy app-only HAR inventory format for existing tests."""
    app_routes = [
        {
            "method": method.http_method,
            "path": method.route,
            "status_codes": list(method.status_codes),
            "sources": list(method.sources),
        }
        for method in metadata
        if method.route.startswith(_MANUAL_APP_ROUTE_PREFIXES)
        or method.route.startswith("/apps/")
    ]
    manual_routes: list[dict[str, Any]] = []
    for method in build_app_method_metadata():
        if not method.http_method or not method.route:
            continue
        manual_routes.append(
            {
                "method": method.http_method,
                "path": method.route,
                "status_codes": [],
                "sources": ["manual_app_runtime"],
            }
        )
        if method.route == "/api/v1.0/app-registry/apps/{include_hidden}":
            manual_routes.append(
                {
                    "method": method.http_method,
                    "path": "/api/v1.0/app-registry/apps/false",
                    "status_codes": [],
                    "sources": ["manual_app_runtime"],
                }
            )
    indexed = {
        (entry["method"], entry["path"]): entry
        for entry in [*app_routes, *manual_routes]
    }
    return [indexed[key] for key in sorted(indexed, key=lambda item: (item[1], item[0]))]


def _load_observed_requests(
    *,
    har_files: Sequence[str | Path],
    registry: SchemaRegistry,
) -> list[_ObservedRequest]:
    observed: list[_ObservedRequest] = []
    for har_file in har_files:
        har_path = Path(har_file).resolve()
        payload = json.loads(har_path.read_text(encoding="utf-8"))
        entries = payload.get("log", {}).get("entries", [])
        if not isinstance(entries, list):
            continue
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            request = entry.get("request", {})
            response = entry.get("response", {})
            if not isinstance(request, dict) or not isinstance(response, dict):
                continue
            method = request.get("method")
            url = request.get("url")
            if not isinstance(method, str) or not isinstance(url, str):
                continue

            parsed_url = urlparse(url)
            raw_path = parsed_url.path or "/"
            normalized_path = _normalize_for_matching(raw_path)
            if (method.upper(), normalized_path) in _SUPPRESSED_SILVER_ROUTES:
                continue
            if registry.match_operation(method, normalized_path):
                continue
            if _is_discarded_candidate(raw_path=raw_path, normalized_path=normalized_path):
                continue

            status_code = response.get("status")
            observed.append(
                _ObservedRequest(
                    method=method.upper(),
                    raw_path=raw_path,
                    normalized_path=normalized_path,
                    source=har_path.name,
                    status_code=status_code if isinstance(status_code, int) else None,
                    query=dict(parse_qsl(parsed_url.query, keep_blank_values=True)),
                    file_fields=_extract_multipart_file_fields(request),
                    body=_parse_request_body(request),
                )
            )
    return observed


def _build_variable_position_map(
    observed: Sequence[_ObservedRequest],
) -> dict[tuple[str, str], set[int]]:
    varying_values: dict[tuple[str, int, int, tuple[str, ...]], set[str]] = defaultdict(set)
    for item in observed:
        segments = _split_segments(item.normalized_path)
        for position, value in enumerate(segments):
            signature = (
                item.method,
                len(segments),
                position,
                tuple(segment for index, segment in enumerate(segments) if index != position),
            )
            varying_values[signature].add(value)

    variable_positions: dict[tuple[str, str], set[int]] = defaultdict(set)
    for item in observed:
        segments = _split_segments(item.normalized_path)
        for position, value in enumerate(segments):
            signature = (
                item.method,
                len(segments),
                position,
                tuple(segment for index, segment in enumerate(segments) if index != position),
            )
            if _looks_like_identifier(value) or (
                len(varying_values[signature]) > 1
                and _can_parameterize_named_segment(segments, position, varying_values[signature])
            ):
                variable_positions[(item.method, item.normalized_path)].add(position)
    return variable_positions


def _template_raw_path(
    raw_path: str,
    normalized_path: str,
    variable_positions: Mapping[tuple[str, str], set[int]],
) -> str:
    normalized_segments = _split_segments(normalized_path)
    raw_segments = _split_segments(raw_path)
    template_positions = variable_positions.get(("GET", normalized_path), set())
    if not template_positions:
        for key, positions in variable_positions.items():
            _, candidate_path = key
            if candidate_path == normalized_path:
                template_positions = positions
                break
    raw_offset = len(raw_segments) - len(normalized_segments)
    rendered: list[str] = []
    for index, segment in enumerate(raw_segments):
        normalized_index = index - raw_offset
        if normalized_index >= 0 and normalized_index in template_positions:
            parameter_name = _path_parameter_name(
                segments=normalized_segments,
                position=normalized_index,
                values=(normalized_segments[normalized_index],),
            )
            rendered.append(f"{{{parameter_name}}}")
        else:
            rendered.append(segment)
    return "/" + "/".join(rendered)


def _namespace_path_from_normalized(normalized_route: str) -> tuple[str, ...]:
    segments = _split_segments(normalized_route)
    if not segments:
        return ("root",)
    if segments[0] == "apps":
        service = to_snake_case(segments[1]) if len(segments) > 1 else "root"
        return ("apps", service)
    return (to_snake_case(segments[0]),)


def _build_method_name(
    *,
    http_method: str,
    namespace_path: tuple[str, ...],
    normalized_route: str,
) -> str:
    segments = _split_segments(normalized_route)
    if namespace_path[0] == "apps":
        relevant = segments[2:]
        if relevant[:1] == ["api"]:
            relevant = relevant[1:]
        if relevant[:1] and to_snake_case(relevant[0]) == namespace_path[-1]:
            relevant = relevant[1:]
    else:
        relevant = segments[1:]

    tokens: list[str] = []
    static_tokens = [
        to_snake_case(token)
        for token in relevant
        if not token.startswith("{")
    ]
    static_count = len([token for token in static_tokens if token])
    if relevant and relevant[0].startswith("{") and namespace_path[0] != "apps":
        tokens.append(_singularize(namespace_path[-1]))

    for token in relevant:
        if token.startswith("{"):
            continue
        normalized = to_snake_case(token)
        if normalized in _NOISY_METHOD_TOKENS and static_count > 1:
            continue
        if normalized:
            tokens.append(normalized)

    if relevant and relevant[-1].startswith("{") and tokens:
        tokens[-1] = _singularize(tokens[-1])

    if not tokens:
        tokens = ["endpoint"]

    return "_".join([http_method.lower(), *tokens])


def _build_path_parameters(
    *,
    route: str,
    normalized_route: str,
    observed_items: Sequence[_ObservedRequest],
) -> list[SilverParameterMetadata]:
    route_segments = _split_segments(route)
    normalized_segments = _split_segments(normalized_route)
    raw_offset = len(route_segments) - len(normalized_segments)
    values_by_name: dict[str, list[str]] = defaultdict(list)
    parameters: list[SilverParameterMetadata] = []
    seen: set[str] = set()

    for index, segment in enumerate(route_segments):
        if not (segment.startswith("{") and segment.endswith("}")):
            continue
        normalized_index = index - raw_offset
        parameter_name = segment[1:-1]
        if parameter_name in seen:
            continue
        seen.add(parameter_name)
        for item in observed_items:
            item_segments = _split_segments(item.normalized_path)
            if normalized_index < len(item_segments):
                values_by_name[parameter_name].append(item_segments[normalized_index])
        parameters.append(
            SilverParameterMetadata(
                python_name=parameter_name,
                api_name=parameter_name,
                location="path",
                required=True,
                type_display=_infer_type_display(values_by_name.get(parameter_name, []), prefer_string=True),
                description=(
                    "Path parameter inferred from HAR observations. This route remains on the "
                    "Silver surface because Stoplight does not publish a Golden contract for it."
                ),
            )
        )
    return parameters


def _build_query_parameters(observed_items: Sequence[_ObservedRequest]) -> list[SilverParameterMetadata]:
    values: dict[str, list[str]] = defaultdict(list)
    presence: dict[str, int] = defaultdict(int)
    for item in observed_items:
        for key, value in item.query.items():
            values[key].append(value)
            presence[key] += 1

    parameters: list[SilverParameterMetadata] = []
    total = len(observed_items)
    for api_name in sorted(values):
        parameters.append(
            SilverParameterMetadata(
                python_name=to_snake_case(api_name),
                api_name=api_name,
                location="query",
                required=presence[api_name] == total,
                type_display=_infer_type_display(values[api_name]),
                description=(
                    "Query parameter inferred from HAR observations for this undocumented "
                    "Silver route."
                ),
            )
        )
    return parameters


def _build_file_parameters(observed_items: Sequence[_ObservedRequest]) -> list[SilverParameterMetadata]:
    presence: dict[str, int] = defaultdict(int)
    for item in observed_items:
        for api_name in item.file_fields:
            presence[api_name] += 1

    if not presence:
        return []

    total = len(observed_items)
    parameters: list[SilverParameterMetadata] = []
    for api_name in sorted(presence):
        parameters.append(
            SilverParameterMetadata(
                python_name="file" if api_name == "File" else to_snake_case(api_name),
                api_name=api_name,
                location="file",
                required=presence[api_name] == total,
                type_display="str | PathLike[str]",
                description=(
                    "Multipart file field inferred from HAR observations for this undocumented "
                    "Silver route. Pass a local file path and the SDK uploads it as form-data."
                ),
            )
        )
    return parameters


def _build_body_parameters(observed_items: Sequence[_ObservedRequest]) -> list[SilverParameterMetadata]:
    bodies = [item.body for item in observed_items if item.body is not None]
    if not bodies:
        return []

    if any(not isinstance(body, dict) for body in bodies):
        return [
            SilverParameterMetadata(
                python_name="json_body",
                api_name="json_body",
                location="body",
                required=True,
                type_display="Mapping[str, Any] | list[Any] | str",
                description=(
                    "Request body observed in HAR traffic. The SDK keeps it as a single payload "
                    "parameter because the undocumented route did not expose a stable object shape."
                ),
            )
        ]

    field_values: dict[str, list[Any]] = defaultdict(list)
    presence: dict[str, int] = defaultdict(int)
    has_complex_field = False
    for body in bodies:
        assert isinstance(body, dict)
        for key, value in body.items():
            field_values[key].append(value)
            presence[key] += 1
            if isinstance(value, (dict, list)):
                has_complex_field = True

    if has_complex_field or len(field_values) > 6:
        return [
            SilverParameterMetadata(
                python_name="json_body",
                api_name="json_body",
                location="body",
                required=True,
                type_display="Mapping[str, Any]",
                description=(
                    "Request body observed in HAR traffic. The SDK uses a single `json_body` "
                    "payload because the Silver route carries a complex undocumented schema."
                ),
            )
        ]

    parameters: list[SilverParameterMetadata] = []
    total = len(bodies)
    for api_name in sorted(field_values):
        parameters.append(
            SilverParameterMetadata(
                python_name=to_snake_case(api_name),
                api_name=api_name,
                location="body",
                required=presence[api_name] == total,
                type_display=_infer_type_display(field_values[api_name]),
                description=(
                    "Body field inferred from HAR observations for this undocumented Silver route."
                ),
            )
        )
    return parameters


def _build_summary(aggregate: _Aggregate) -> str:
    namespace = ".".join(aggregate.namespace_path)
    return (
        f"HAR-derived undocumented {aggregate.method} route for `client.silver.{namespace}`."
    )


def _build_description(aggregate: _Aggregate) -> str:
    return (
        "This method is intentionally kept on the Silver surface because bundled Stoplight "
        "controller contracts do not define this route. Golden Stoplight operations remain the "
        "preferred contract source whenever they exist, so Silver only supplements gaps "
        "observed in tenant HAR traffic."
    )


def _dedupe_method_names(
    methods: Sequence[SilverMethodMetadata],
) -> tuple[SilverMethodMetadata, ...]:
    counts: dict[tuple[tuple[str, ...], str], int] = defaultdict(int)
    deduped: list[SilverMethodMetadata] = []
    for method in methods:
        key = (method.namespace_path, method.method_name)
        count = counts[key]
        counts[key] += 1
        if count == 0:
            deduped.append(method)
            continue
        deduped.append(
            SilverMethodMetadata(
                namespace_path=method.namespace_path,
                method_name=f"{method.method_name}_{count + 1}",
                http_method=method.http_method,
                route=method.route,
                parameters=method.parameters,
                summary=method.summary,
                description=method.description,
                typed_return=method.typed_return,
                raw_return=method.raw_return,
                sources=method.sources,
                status_codes=method.status_codes,
                uses_app_headers=method.uses_app_headers,
            )
        )
    return tuple(deduped)


def _manual_app_routes() -> set[tuple[str, str]]:
    return {
        (method.http_method, _route_shape(method.route))
        for method in build_app_method_metadata()
        if method.http_method and method.route
    }


def _normalize_for_matching(path: str) -> str:
    if path.startswith("/api/v1.0"):
        path = path[len("/api/v1.0") :] or "/"
    if path != "/":
        path = path.rstrip("/") or "/"
    return path


def _parse_request_body(request: Mapping[str, Any]) -> Any | None:
    post_data = request.get("postData")
    if not isinstance(post_data, Mapping):
        return None
    mime_type = post_data.get("mimeType")
    if isinstance(mime_type, str) and mime_type.lower().startswith("multipart/form-data"):
        return None
    body_text = post_data.get("text")
    if not isinstance(body_text, str) or not body_text.strip():
        return None
    try:
        return json.loads(body_text)
    except json.JSONDecodeError:
        return body_text


def _extract_multipart_file_fields(request: Mapping[str, Any]) -> tuple[str, ...]:
    post_data = request.get("postData")
    if not isinstance(post_data, Mapping):
        return ()
    mime_type = post_data.get("mimeType")
    if not isinstance(mime_type, str) or not mime_type.lower().startswith("multipart/form-data"):
        return ()
    params = post_data.get("params")
    if not isinstance(params, list):
        return ()

    file_fields: list[str] = []
    for parameter in params:
        if not isinstance(parameter, Mapping):
            continue
        name = parameter.get("name")
        value = parameter.get("value")
        if isinstance(name, str) and value == "(binary)":
            file_fields.append(name)
    return tuple(sorted(dict.fromkeys(file_fields)))


def _is_discarded_candidate(*, raw_path: str, normalized_path: str) -> bool:
    if normalized_path in _DISCARD_EXACT:
        return True
    if any(normalized_path.startswith(prefix) for prefix in _DISCARD_PREFIXES):
        return True
    if normalized_path.startswith("/apps/") and (
        "/app/" in normalized_path or "/img/" in normalized_path or normalized_path.endswith(_STATIC_SUFFIXES)
    ):
        return True
    if normalized_path.endswith(_STATIC_SUFFIXES):
        return True
    if "/img/" in normalized_path:
        return True
    return raw_path == "/%7B%7B%20$ctrl.IconUri%20%7D%7D"


def _split_segments(path: str) -> list[str]:
    return [segment for segment in path.split("/") if segment]


def _looks_like_identifier(value: str) -> bool:
    return bool(_UUID_RE.fullmatch(value) or _INT_RE.fullmatch(value) or _BOOL_RE.fullmatch(value))


def _can_parameterize_named_segment(
    segments: Sequence[str],
    position: int,
    values: Collection[str],
) -> bool:
    if any(_looks_like_identifier(value) for value in values):
        return True
    previous = next((segments[index] for index in range(position - 1, -1, -1)), "")
    next_segment = next((segments[index] for index in range(position + 1, len(segments))), "")
    return (
        to_snake_case(previous) in _PARAMETER_HINTS
        or to_snake_case(next_segment) in _PARAMETER_HINTS
    )


def _path_parameter_name(
    *,
    segments: Sequence[str],
    position: int,
    values: Sequence[str],
) -> str:
    if (
        len(segments) >= 3
        and position == 1
        and segments[0] == "profiles"
        and segments[2] == "picture"
    ):
        return "user_id"
    previous = next((segments[index] for index in range(position - 1, -1, -1) if not segments[index].startswith("{")), "")
    next_segment = next(
        (segments[index] for index in range(position + 1, len(segments)) if not segments[index].startswith("{")),
        "",
    )
    base = to_snake_case(previous or next_segment or f"segment_{position + 1}")
    if base == "serial":
        return "serial"
    if base == "app" and any(not _looks_like_identifier(value) for value in values):
        return "app_key"
    base = _singularize(base)
    if base.endswith("_id") or base.endswith("_key"):
        return base
    if any(not _looks_like_identifier(value) for value in values):
        return f"{base}_key"
    return f"{base}_id"


def _route_shape(path: str) -> str:
    return re.sub(r"\{[^}]+\}", "{}", path)


def _infer_type_display(values: Sequence[Any], *, prefer_string: bool = False) -> str:
    non_null_values = [value for value in values if value is not None]
    if not non_null_values:
        return "str | None" if prefer_string else "Any | None"
    if all(isinstance(value, bool) or (isinstance(value, str) and _BOOL_RE.fullmatch(value)) for value in non_null_values):
        return "bool"
    if all(isinstance(value, int) or (isinstance(value, str) and _INT_RE.fullmatch(value)) for value in non_null_values):
        return "int"
    if all(isinstance(value, (int, float)) for value in non_null_values):
        return "float"
    return "str"


def _uses_app_headers(route: str) -> bool:
    return route.startswith("/apps/") or route.startswith("/api/v1.0/app-registry/") or route.startswith(
        "/api/v1.0/apps/"
    )


def _singularize(value: str) -> str:
    if value.endswith("ies") and len(value) > 3:
        return f"{value[:-3]}y"
    if value.endswith("ses") and len(value) > 3:
        return value[:-2]
    if value.endswith("s") and not value.endswith("ss") and len(value) > 1:
        return value[:-1]
    return value
