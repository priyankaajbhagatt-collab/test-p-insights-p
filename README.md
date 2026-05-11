# test-p-insights-p

test-p-insights-p

Generated from the Backstage `python-service` scaffolder template.

- **Group:** `commerce/orderas`
- **Markets:** `usa`, `can`
- **Owner:** `user:guest`

## Local development

```bash
pip install -e ".[dev]"
uvicorn app.main:app --reload
curl http://localhost:8000/
```

## CI/CD

- `.github/workflows/ci.yml` — lint + test + image build on every push and PR.
- `.github/workflows/cd.yml` — deploy across the configured markets (usa, can) on push to `main`.

## Backstage views

This service is registered in Backstage and surfaces:

- Pipeline Triage
- DORA Metrics
- Failure Intelligence
- Market Deployments

at both the unit (service) and group (`commerce/orderas`) level.
