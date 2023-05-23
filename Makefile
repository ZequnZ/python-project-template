venv:
	pyenv activate pyproj

install-dev:
	pip install -r requirements/dev.txt

checker:
	mypy ./src

lint:
	ruff check ./src
	black ./src --check

format:
	ruff check ./src --fix
	black ./src -v

test:
	pytest ./src/test
