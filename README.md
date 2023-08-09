# Python project template

A template for **Python project**, equipped with best practices, can be used whenever needed.

## Highlights

### 🛠️ Reproducible development environment:
- Python version management tool: [pyenv](https://github.com/pyenv/pyenv)
- Python packaging and dependency management: [Poetry](https://python-poetry.org/)
- [TODO] Dockerfile: test and run codes within container
- Makefile: provides shortcuts to making life easier

### 🧹 Maintain a clean code style
- Type checker: [mypy](https://github.com/python/mypy)
- Code formatter:[black](https://github.com/psf/black)
- Linter: [ruff](https://github.com/charliermarsh/ruff).  Rules→[here](https://beta.ruff.rs/docs/rules/)
- Import sorter: [isort](https://pycqa.github.io/isort/)

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
    -black [link](https://black.readthedocs.io/en/stable/integrations/source_version_control.html)
    - ruff [link](https://beta.ruff.rs/docs/tutorial/#continuous-integration)

### 📝 Github Features:
- PR template
- Issue template


## Guidebook

### Create a reproducible Python development environment with *pyenv* and *Poetry*
Here I use a Python version management tool: [pyenv](https://github.com/pyenv/pyenv).
As a user, we can easily install and switch between different versions of Python.
You can install pyenv following [this link](https://github.com/pyenv/pyenv#getting-pyenv).

[Poetry](https://python-poetry.org/) is a great tool for Python packaging and dependency management, as a user you can easily reproduce the development environment and update the packages when possible, especially when it is already being used - which is the case for this project.
You can install Poetry following [this link](https://python-poetry.org/docs/#installation), after setting the Python version as mentioned above.

Then we can create a Python virtual env as follows:
1. Install a specific verion of Python:
```
    # Install Python 3.10.6 as an example
    pyenv install 3.10.6
```

**[Deprecated]**, use Poetry for setting virtual environment and dependency management
~~2. Create a virtual env, with Python verison and customized name:~~
```
    pyenv virtualenv <python_version> <environment_name>
```
~~3. After installation, you will be able to activate and deactivate the env:~~
```
    # Activate
    pyenv activate <environment_name>
    # Deactivate
    source deactivate
```
~~Activating your env to maintain a stable development environment.~~

And then, you just need:
2. Create a virtual environment and install dependency:
```
poetry install
```

## TODO

- Docker compose for spin-up different components:
    - DB
    - Kafka

- CI:


Reference:
- https://github.com/TezRomacH/python-package-template
- https://github.com/stevemao/github-issue-templates
