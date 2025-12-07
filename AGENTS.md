# Project instructions

This is a modern Python project template designed with best practices for maintainable, scalable Python applications.

## Project Overview

### Technology Stack
- **Python**: 3.12+ (managed by uv)
- **Package Management**: [uv](https://docs.astral.sh/uv/) - extremely fast Python package manager
- **Testing**: pytest with coverage reporting
- **Linting & Formatting**: Ruff (replaces black, isort, flake8)
- **Task Runner**: [Task](https://taskfile.dev/) (replaces Makefiles)
- **Pre-commit**: Automated code quality checks
- **Configuration**: Pydantic Settings with environment-based configs
- **Containerization**: Docker with uv support
- **CI/CD**: GitHub Actions with caching

### Project Structure
```
src/
├── python_project_template/    # Main package directory
│   ├── __init__.py
│   └── configuration/          # Pydantic-based configuration management
│       ├── __init__.py
│       ├── config_settings.py  # Environment-specific settings
└── test/                       # Test suite
    ├── conftest.py             # Pytest fixtures and configuration
    └── test_*.py               # Test files
```

## Development Guidelines

### Environment Setup
- Use `uv sync` to install dependencies and create virtual environment
- Activate with `source .venv/bin/activate` or use `uv run <command>`
- All commands should be prefixed with `uv run` when outside activated environment

### Code Style & Quality
- **Import style**: Use Ruff's isort-compatible import sorting
- **Type hints**: Required for all public functions and methods
- **Type checking**: Project uses multiple type checkers:
  - ty for fast Rust-based type checking (configuration in `ty.toml`)
  - pyrefly for advanced type analysis with granular error control (configuration in `pyrefly.toml`)
- **Docstrings**: Use Google-style docstrings for classes and functions

### Testing Practices
- Tests located in `src/test/` directory
- Use pytest markers for test categorization:
  - `@pytest.mark.slow` for slow tests
  - `@pytest.mark.test_mark` for testing purposes
- Test coverage target: 80%+
- Run tests with: `uv run pytest ./src/test`

### Configuration Management
- Use Pydantic Settings for all configuration
- Environment-specific configs in `pyproject.toml` under `[config.<env>]`
- Required environment variable: `ENVIRONMENT` (e.g., "local", "dev", "prod")
- Configuration priority order:
  1. CLI arguments
  2. Environment-specific pyproject.toml table
  3. Default pyproject.toml table
  4. Environment variables

### Available Tasks (Taskfile.yml)
- `task linter`: Run Ruff linter with auto-fix
- `task linter-watch`: Run Ruff linter in watch mode
- `task formatter`: Run Ruff formatter
- `task ty-checker`: Run ty type checker (fast Rust-based)
- `task pyrefly-checker`: Run pyrefly type checker (advanced analysis)
- `task run-test`: Execute test suite
- `task precommit`: Run pre-commit hooks
- `task check_updatable_libs`: Check for dependency updates
- `task dc-up`: Start docker compose services
- `task dc-exec`: Execute command in running container


### For configuration-related code:
1. Extend `SourceSettings` or `BasicSettings` classes
2. Use `Field` with `alias` for environment variable mapping
3. Include proper type annotations
4. Add validation methods when necessary

### Docker considerations:
- Use multi-stage builds when possible
- Install dependencies with `uv sync --frozen`
- Set `ENVIRONMENT` variable appropriately
- Mount source code as volumes for development

### Dependencies:
- Add runtime dependencies with: `uv add package-name`
- Add dev dependencies with: `uv add --group dev package-name`
- Keep dependencies minimal and well-justified
- Pin major versions for stability

## Pre-commit and CI/CD

### Pre-commit hooks run:
- Trailing whitespace removal
- End-of-file fixing
- YAML/TOML validation
- Ruff linting and formatting
- UV dependency validation

### CI pipeline includes:
- Multi-OS testing (Ubuntu, macOS)
- Python 3.12
- Dependency caching
- Pre-commit hook validation
- Full test suite execution

## Best Practices

1. **Test-driven development** - Write tests for new functionality
2. **Small, focused commits** - Use conventional commit messages
3. **Environment variables** - Never hardcode configuration values
4. **Error handling** - Use proper exception handling and logging
5. **Performance** - Leverage uv's speed for dependency operations
6. **Security** - Use `safety` for vulnerability scanning

## Common Patterns

### Adding a new configuration setting:
```python
class BasicSettings(SourceSettings):
    new_setting: str = Field(
        alias="NEW_SETTING",
        description="Description of the setting"
    )
```

### Creating a new test:
```python
import pytest

def test_new_functionality():
    # Arrange
    expected = "expected_value"

    # Act
    result = function_under_test()

    # Assert
    assert result == expected
```

### Adding a new dependency:
```bash
# Runtime dependency
uv add package-name

# Development dependency
uv add --group dev package-name
```

Remember: This template prioritizes developer experience, code quality, and maintainability. All suggestions should align with these principles.
