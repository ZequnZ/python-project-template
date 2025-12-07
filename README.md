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
- Type checkers: 
  - [ty](https://github.com/pyrefly/pyrefly) - Fast type checker built in Rust (configured in `ty.toml`)
  - [pyrefly](https://github.com/pyrefly/pyrefly) - Advanced type checker with granular control (configured in `pyrefly.toml`)
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


### 📝 Github Features:
- PR template
- Issue template
- CI workflow

### 🤖 AI tool instructions:
- [AGENTS.md](./AGENTS.md) - agent instructions for the project
- Github Copilot instructions are added in [.github](./.github)
- Cursor rules are added in [.cursor](./cursor)

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

### Available Task commands

The project uses [Task](https://taskfile.dev/) as a task runner. Here are the available commands:

**Code Quality:**
```bash
task linter           # Run ruff linter with auto-fix
task linter-watch     # Run ruff linter in watch mode
task formatter        # Run ruff formatter
task ty-checker       # Run ty type checker (fast Rust-based)
task pyrefly-checker  # Run pyrefly type checker (advanced analysis)
task precommit        # Run all pre-commit hooks
```

**Testing:**
```bash
task run-test         # Run test suite in src/test folder
```

**Dependency Management:**
```bash
task check_updatable_libs  # Check for outdated dependencies
```

**Docker:**
```bash
task dc-up            # Start docker compose services
                      # Usage: task dc-up PROFILE=<name> BUILD=--build
task dc-exec          # Execute command in running container
                      # Usage: task dc-exec SERVICE=<name> CMD=<command>
```

## TODO

- Docker compose for spin-up different components:
    - DB
    - Kafka

- CI:


Reference:
- https://github.com/TezRomacH/python-package-template
- https://github.com/stevemao/github-issue-templates
