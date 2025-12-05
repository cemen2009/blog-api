########## 1. build stage ##########
FROM python:3.13-slim AS builder

# install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

    # tells uv to compile Python files to bytecode for faster startup
ENV UV_COMPILE_BYTECODE=1 \
    # ensures uv copies files instead of creating symlinks
    UV_LINK_MODE=copy

# copy only dependency descriptors — leverage Docker cache
COPY pyproject.toml uv.lock ./

# install dependencies (without installing project code yet)
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --no-install-project

# copy only the application source code (the src/ directory)
COPY src/ ./

# install the project (non-editable), so src/ is installed into venv/site-packages
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

########## 2. production stage ##########
FROM python:3.13-slim AS runtime

ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# copy venv (or site‑packages + bin) from build
COPY --from=builder --chown=appuser:appgroup /app /app

# create non-root user
RUN groupadd -g 1001 appgroup && \
    useradd -u 1001 -g appgroup -m -d /app -s /bin/false appuser

USER appuser


CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
