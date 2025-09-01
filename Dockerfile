# Multi-stage build
FROM python:3.12-slim AS base

ARG UV_VERSION=0.8.14

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    # Keeps Python from generating .pyc files in the container
    PYTHONDONTWRITEBYTECODE=1 \
    # Turns off buffering for easier container logging
    PYTHONUNBUFFERED=1

# WORKDIR /app

FROM base AS builder

ENV UV_VERSION=${UV_VERSION} \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

# Disable Python downloads, because we want to use the system interpreter
# across both images. If using a managed Python version, it needs to be
# copied from the build image into the final image; see `standalone.Dockerfile`
# for an example.
ENV UV_PYTHON_DOWNLOADS=0

# Install uv
RUN pip install --no-cache-dir "uv==${UV_VERSION}"

ARG DEPENDENCY_INSTALL_OPTION="--no-dev"
# Install Python dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project ${DEPENDENCY_INSTALL_OPTION}

FROM base AS final

ENV UV_VERSION=${UV_VERSION} \
    VIRTUAL_ENV=/.venv \
    PATH="/.venv/bin:${PATH}" \
    PYTHONPATH="/app/src/"

WORKDIR /app

# Copy installed Python dependencies to final container
COPY --from=builder /.venv ${VIRTUAL_ENV}

# Copy your code into container
COPY src/ /app/src/

# This is needed to for running locally
ARG INSTALL_UV=false
RUN bash -c "if [ $INSTALL_UV == 'true' ] ; then pip install 'uv==$UV_VERSION' ; fi"
