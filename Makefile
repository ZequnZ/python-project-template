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

precommit:
	poetry run pre-commit run

docker-build:
	docker build py-proj-template .

docker-run:
	docker run --name py-proj-template -itd py-proj-template

docker-exec:
	docker exec -it py-proj-template bash

docker-stop:
	docker stop  py-proj-template
