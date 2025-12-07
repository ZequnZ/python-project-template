# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## Current version [0.4.0] - 2025-12-07

### Added
- Advanced type checking support with [ty](https://github.com/pyrefly/pyrefly) and [pyrefly](https://github.com/pyrefly/pyrefly)
  - `ty.toml` configuration for fast Rust-based type checking
  - `pyrefly.toml` configuration for granular type checking control
  - Both tools added as dev dependencies in `pyproject.toml`
- Project now configured as a proper Python package with build system support
  - Added `build-system` configuration in `pyproject.toml` using hatchling
  - Removed `[tool.uv] package = false` to enable package mode

### Changed
- **Project structure reorganization**:
  - Moved source code from `src/configuration/` to `src/python_project_template/configuration/`
  - Added proper package structure with `__init__.py` files
  - Updated import paths in configuration modules to use package-relative imports
- Removed unnecessary dependencies:
  - `psutil` removed from safety dependencies
  - `setuptools` removed (no longer needed with modern build systems)
  - `sniffio` removed (unused transitive dependency)

### Migration Notes
- If you're importing from this project, update imports from `src.configuration` to `src.python_project_template.configuration`
- The project can now be built and installed as a proper Python package using `uv build` or `pip install .`
- Type checking can now be performed with three different tools:
  - `uv run ty check` for fast Rust-based checking
  - `uv run pyrefly` for advanced type analysis

## [0.3.0] - 2025-09-09

### Added
- Comprehensive AI coding instructions and development guidelines
- `.cursor/rules/python_guidelines.mdc` - Cursor AI editor rules with Python coding standards
- `.cursorrules` - Main Cursor AI editor configuration file
- `.github/ISSUE_TEMPLATE/instructions/python.instructions.md` - GitHub issue template instructions
- `.github/copilot-instructions.md` - GitHub Copilot specific instructions for the project template
- `.github/prompts/create-pr-description.prompt.md` - Automated PR description generation template
- Multi-platform AI assistant support (Cursor, GitHub Copilot, general AI)
- Standardized Python 3.12+ coding practices and conventions
- Type hints and comprehensive documentation requirements
- Error handling and edge case management guidelines
- Modern development tool integration (Ruff, pytest, uv, Docker)

### Changed
- Renamed `src/configuration/config_test.py` to `src/configuration/config_example.py` for better clarity and naming convention

## [0.2.0] - 2025-08-31

### Changed
- **BREAKING**: Migrated from Poetry to [uv](https://docs.astral.sh/uv/) for Python package and dependency management
- **BREAKING**: Updated minimum Python version from 3.10 to 3.12
- Updated `pyproject.toml` to use modern PEP 621 format instead of Poetry-specific format
- Updated Docker configuration to use uv instead of Poetry
- Updated all task runner commands in `Taskfile.yml` to use `uv run` instead of `poetry run`
- Updated pre-commit configuration to use direct ruff and uv integrations
- Updated Python base image in Dockerfile from 3.10.6-slim to 3.12-slim
- Updated README.md documentation to reflect uv usage and simplified setup process
- Updated GitHub Actions CI workflow to use uv instead of Poetry and Python 3.12

### Added
- uv pre-commit hook for automatic dependency lock file updates
- Enhanced Docker build with better caching and optimization
- Dependency update checking in pre-commit hooks

### Removed
- Poetry dependency management (`poetry.lock` removed, replaced with `uv.lock`)
- Makefile (already deprecated in favor of `Taskfile.yml`)
- pyenv references from documentation (uv handles Python installation)

### Fixed
- Docker container now properly copies source code and sets up environment
- Improved development environment reproducibility with uv

## [0.0.3] - 2024-11-16
Added:
- Github Workflow: CI, runs for PR
- Add [pyupgrade](https://github.com/asottile/pyupgrade) for ruff
- Add configuration management(based on [Pydantic-settings](https://github.com/pydantic/pydantic-settings))

## [0.0.2] - 2024-07-23

Added:
- Task runner `Task`
- Update libs
- Update pre-commit using Task

Removed:
- black and isort, as Ruff now provides functionalies to cover them
- Makefile, replaced by Taskfile

## [0.0.1] - 2022-04-20
Added: Changelog & TODO list
