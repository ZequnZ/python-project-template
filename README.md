# Python project template

A template for **Python project**, equipped with best practices, can be used whenever needed.

[![CI](https://github.com/ZequnZ/python-project-template/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/ZequnZ/python-project-template/actions?query=event%3Apush+branch%3Amain+workflow%3ACI)

## Highlights

### 🛠️ Reproducible development environment:
- Python packaging and dependency management: [uv](https://docs.astral.sh/uv/) (handles Python installation and virtual environments)
- Dockerfile: test and run codes within container
- ~~Makefile: provides shortcuts to making life easier~~ Deprecated, replaced by Task
- Task runner [Task](https://taskfile.dev/): easily run pre-defined tasks specified in configuration file [Taskfile.yml](./Taskfile.yml)

### 🧹 Maintain a clean code style
- Type checker: [mypy](https://github.com/python/mypy)
- Linter & Formatter: [Ruff](https://github.com/charliermarsh/ruff).  Rules→[here](https://beta.ruff.rs/docs/rules/)
- ~~Code formatter:[black](https://github.com/psf/black)~~ Deprecated, covered by Ruff.
- ~~Import sorter: [isort](https://pycqa.github.io/isort/)~~ Deprecated, covered by Ruff.

### 🩺 Testing framework [pytest](https://docs.pytest.org/en/7.4.x/)
- Running test: `pytest ./src/test`
- Test on specific marker: `pytest ./src/test -m <mark_name>`
- Test + duration report: `pytest ./src/test --durations=3`
- Test + coverage: `pytest --cov=src ./src/test`
- Test + force coverage: `pytest --cov-fail-under=80 ./src/test`

### 🪄 pre-commit hook:
- Run [.pre-commit-config.yaml](./.pre-commit-config.yaml) every time before submission to ensure quality
- Install pre-commit: [link](https://pre-commit.com/#install)
- Generate & modify [.pre-commit-config.yaml](./.pre-commit-config.yaml)
- Set up the git hook scripts: `pre-commit install`
- TODO:
    - ~~black [link](https://black.readthedocs.io/en/stable/integrations/source_version_control.html)~~
    - ruff [link](https://beta.ruff.rs/docs/tutorial/#continuous-integration)

### 📝 Github Features:
- PR template
- Issue template
- CI workflow

### 🔫 Security check:
- Dependency vulnerability check:[safety](https://github.com/pyupio/safety), support CLI and in CI workflow

## Guidebook

### Create a reproducible Python development environment with *uv*

[uv](https://docs.astral.sh/uv/) is an extremely fast Python package and project manager that handles both Python installation and dependency management. It's all you need to set up a reproducible development environment for this project.

You can install uv following [this link](https://docs.astral.sh/uv/getting-started/installation/).

Setting up the development environment is simple:

1. **Install Python and create virtual environment with dependencies:**
```bash
uv sync
```

That's it! uv will automatically:
- Install Python 3.12+ if not available (as specified in `pyproject.toml`)
- Create a virtual environment in `.venv/`
- Install all project dependencies and development tools

2. **Activate the virtual environment:**
```bash
source .venv/bin/activate
```

3. **Run commands within the environment:**
```bash
# Run tests
uv run pytest ./src/test

# Run linting
uv run ruff check

# Add new dependencies
uv add <package-name>

# Add development dependencies
uv add --group dev <package-name>
```

## TODO

- Docker compose for spin-up different components:
    - DB
    - Kafka

- CI:


Reference:
- https://github.com/TezRomacH/python-package-template
- https://github.com/stevemao/github-issue-templates
