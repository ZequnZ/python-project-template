# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## Current version [0.2.0] - 2025-08-31

### Changed
- **BREAKING**: Migrated from Poetry to [uv](https://docs.astral.sh/uv/) for Python package and dependency management
- **BREAKING**: Updated minimum Python version from 3.10 to 3.12
- Updated `pyproject.toml` to use modern PEP 621 format instead of Poetry-specific format
- Updated Docker configuration to use uv instead of Poetry
- Updated all task runner commands in `Taskfile.yml` to use `uv run` instead of `poetry run`
- Updated pre-commit configuration to use direct ruff and uv integrations
- Updated Python base image in Dockerfile from 3.10.6-slim to 3.12-slim
- Updated README.md documentation to reflect uv usage and simplified setup process

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
