# python-project-template
A template for Python project

I would create a template for Python project, so that some best practices can be picked and used whenever needed.  

## Guidebook

### Create a Python virtual env with *pyenv*
Here I use a Python version management tool: [pyenv](https://github.com/pyenv/pyenv). 
As a user, we can easily install and switch between different versions of Python.
You can install Pyenv following [this link](https://github.com/pyenv/pyenv#getting-pyenv).  

Then we can create a Python virtual env as follows:
1. Install a specific verion of Python:
```
    # Install Python 3.10.4 as an example
    pyenv install 3.10.4 
```
2. Create a virtual env, with Python verison and customized name:
```
    pyenv virtualenv <python_version> <environment_name> 
```
3. After installation, you will be able to activate and deactivate the env:
```
    # Activate
    pyenv activate <environment_name>
    # Deactivate
    source deactivate
```
Activating your env to maintain a stable development environment.


## TODO
- reproducible development environment: 
    - list packages: requirements.txt  
    - dev env: 1. virtual env; 2. Docker  
    - config file: pyproject.toml  
    - Makefile  

- Linter, formatter and type checker:
    - type checker: https://github.com/python/mypy  
    - code formatter: https://github.com/psf/black  
    - linter: https://github.com/charliermarsh/ruff.  Rules→[here](https://beta.ruff.rs/docs/rules/)

- Testing:
    - pytest

- pre-commit hook:

- Docker compose for spin-up different components:
    - DB
    - Kafka

- CI:

- Github Features:


reference:
https://github.com/TezRomacH/python-package-template  
