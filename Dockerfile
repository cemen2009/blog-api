#### Builder for dependencies ####
FROM ghcr.io/astral-sh/uv:latest AS uvbin

#### Base Python + uv binary ####
FROM python:3.13-slim AS builder
COPY --from=uvbin /uv /uvx /bin/

WORKDIR /app
COPY pyproject.toml uv.lock ./

RUN uv sync --frozen

#### Runtime stage ####
FROM python:3.13-slim AS runtime
COPY --from=uvbin /uv /uvx /bin/

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv

ENV PATH="/app/.venv/bin:$PATH"

COPY commands ./commands
COPY src .

CMD ["bash", "commands/run_uvicorn_server.sh"]
