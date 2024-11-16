# Multi-stage build
FROM python:3.10.6-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    # Keeps Python from generating .pyc files in the container
    PYTHONDONTWRITEBYTECODE=1 \
    # Turns off buffering for easier container logging
    PYTHONUNBUFFERED=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# WORKDIR /app

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.7.1

# Install poetry
RUN pip install "poetry==$POETRY_VERSION"

# Copy poetry dependency files to container
COPY pyproject.toml poetry.lock /

ARG POETRY_INSTALL_OPTION="--only main"
# Install dependency
RUN poetry config virtualenvs.in-project true && \
    poetry install -vvv --no-root ${POETRY_INSTALL_OPTION} && \
    rm -rf $POETRY_CACHE_DIR

FROM base as final

ENV VIRTUAL_ENV=/.venv \
    PATH="/.venv/bin:${PATH}" \
    PYTHONPATH="/app/src/"

WORKDIR /app

# Copy installed Python dependencies to final container
COPY --from=builder /.venv ${VIRTUAL_ENV}

# Keep the container running
CMD tail -f /dev/null

# Copy your code into container. e.g.:
# COPY /src /app

# Replace your enterpoint here. e.g:
# ENTRYPOINT ["python", "-m", "main"]
