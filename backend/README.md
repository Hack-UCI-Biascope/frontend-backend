# backend

The fast and efficient backend that powers Biascope

## Initial Setup

### Python & Poetry

We're currently using Python 3.9.
We use [Poetry](https://python-poetry.org/docs/) for Python dependency management. 
Ensure you have Python 3.9.* installed and set up, along with Poetry. 
Click [here](https://python-poetry.org/docs/#installation) for Poetry installation instructions.

### Dev Tools

[PyCharm](https://www.jetbrains.com/pycharm/) is in my (Ravi's) opinion the best IDE for developing with Python. If you choose to use Pycharm for this project, you'll need to download the following plugins:

- [Poetry](https://plugins.jetbrains.com/plugin/14307-poetry)
- [Toml](https://plugins.jetbrains.com/plugin/8195-toml)
- [Code With Me](https://plugins.jetbrains.com/plugin/14896-code-with-me) (Optional)

### Getting Started

The first thing you should do after cloning this repo is install the Poetry dependencies by running `poetry install`. 
Once you have the dependencies installed, you can now spawn a virtualenv shell by running `poetry shell`. 
Whenever working on the project you should always use the `poetry shell`.

## Development

### Code Format & Linting

We use [black](https://github.com/psf/black), [flake8](https://flake8.pycqa.org/en/latest/), [isort](https://github.com/PyCQA/isort), and [mypy](https://github.com/python/mypy) to ensure that code quality is high and style is consistent.

[comment]: <> (We also use [bandit]&#40;https://bandit.readthedocs.io/&#41; to check for common security issues. &#40;work in progress&#41;)

#### Commands:

If running any of these command **outside** of the poetry shell, prepend `poetry run `. For example, format would be `poetry run f`.

- `format`/`f` - automatically formats code and sorts imports.

[comment]: <> (  - This command eliminates the need for you to format your code, just run it before you commit and as you develop to ensure your code style is consistent with the project!)

- `lint`/`l` - lints code and checks for any issues.

- `format-lint`/`fl` - runs `format` then `lint`.

### Testing

We use [pytest](https://docs.pytest.org/) and write tests to ensure code works the way it should. Functions in the `app/tests/` folder with names prefixed with `test_` will be automatically collected and ran by pytest.

#### Commands:

If running any of these command **outside** of the poetry shell, prepend `poetry run `. For example, test would be `poetry run t`.

- `test`/`t` - runs the testing suite

- `format-lint-test`/`flt` - formats and lints code then runs the testing suite
