---
description: 'Python coding conventions and guidelines'
applyTo: '**/*.py'
---

# Python Coding Conventions

## Python Instructions

- Target Python 3.12+ features and syntax.
- Write clear and concise comments for each function.
- Ensure functions have descriptive names and include type hints.
- Provide docstrings following PEP 257 conventions.
- Use the `typing` module for type annotations (e.g., `List[str]`, `Dict[str, int]`).
- Break down complex functions into smaller, more manageable functions.

## General Instructions

- Always prioritize readability and clarity.
- For algorithm-related code, include explanations of the approach used.
- Write code with good maintainability practices, including commensts on why certain design decisions were made.
- Handle edge cases and write clear exception handling.
- For libraries or external dependencies, mention their usage and purpose in comments.
- Use consistent naming conventions and follow language-specific best practices.
- Write concise, efficient, and idiomatic code that is also easily understandable.
- [uv](https://docs.astral.sh/uv/) is used as Python package manager:
    - Use `uv sync` to install dependencies and create virtual environment
    - Activate with `source .venv/bin/activate` or use `uv run <command>`
    - All commands should be prefixed with `uv run` when outside activated environment

### When creating new Python files:
1. Include proper type hints for all function parameters and return types
2. Add docstrings for classes and public methods
3. Follow the existing import order (standard library, third-party, local)
4. Use Pydantic models for data validation when appropriate
    
## Code Style and Formatting

- Follow the **PEP 8** style guide for Python.
- Maintain proper indentation (use 4 spaces for each level of indentation).
- Ensure lines do not exceed 88 characters(Black-compatible).
- Place function and class docstrings immediately after the `def` or `class` keyword.
- Use blank lines to separate functions, classes, and code blocks where appropriate.
- Do not leave whitespace from black line -> `W293 Blank line contains whitespace`
- [ruff](https://docs.astral.sh/ruff/) is used as linter and formatter:
    - Use `uv run ruff check <PATH>` to check for linting issues
    - Use `uv run ruff check <PATH> --fix` to automatically fix linting issues

## Edge Cases and Testing

- Always include test cases for critical paths of the application.
- Account for common edge cases like empty inputs, invalid data types, and large datasets.
- Include comments for edge cases and the expected behavior in those cases.
- Write unit tests for functions and document them with docstrings explaining the test cases.

### For test files:
1. Name test files with `test_` prefix
2. Use descriptive test function names
3. Leverage pytest fixtures from `conftest.py`
4. Use parametrized tests for multiple test cases
5. Add appropriate markers for test categorization


## Example of Proper Documentation

```python
def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle given the radius.
    
    Parameters:
    radius (float): The radius of the circle.
    
    Returns:
    float: The area of the circle, calculated as π * radius^2.
    """
    import math
    return math.pi * radius ** 2
```
