# Security Policy

## Supported Versions

Only the latest minor/patch release line is actively supported.

## Reporting a Vulnerability

Do not open public issues for undisclosed vulnerabilities.

Report security concerns privately to the project maintainers with:
- affected version
- impact summary
- reproduction details
- any known mitigation

Maintainers will acknowledge receipt, assess severity, and coordinate a fix/release.

## Secret Handling

- Never commit `INCIDENTIQ_API_TOKEN` or `INCIDENTIQ_TEST_API_TOKEN`.
- Never log Authorization header values.
- Use `.env.example` as the template for local setup.
