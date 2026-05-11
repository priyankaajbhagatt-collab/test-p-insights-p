from fastapi import FastAPI

app = FastAPI(title="test-p-insights-p")


@app.get("/")
def hello() -> dict[str, str]:
    return {"message": "Hello from test-p-insights-p"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
