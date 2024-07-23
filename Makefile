activate-virtualenv:
	poetry shell

install-dependency:
	poetry install

checker:
	poetry run mypy ./src --check-untyped-defs

linter:
	poetry run ruff check ./src

formatter:
	poetry run ruff check ./src --fix

test:
	poetry run pytest -sv ./src/test

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
