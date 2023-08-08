activate-virtualenv:
	poetry shell

install-dependency:
	poetry install

checker:
	poetry run mypy ./src --check-untyped-defs

linter:
	poetry run black ./src --check
	poetry run ruff check ./src

formatter:
	poetry run black ./src -v
	poetry run ruff check ./src --fix
	poetry run isort ./src -v

test:
	poetry run pytest ./src/test
