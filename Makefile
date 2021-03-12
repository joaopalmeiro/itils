# Source: https://github.com/trickeydan/cookiecutter-awesome-poetry
.PHONY: all check type isort black lint bandit format

CMD:=poetry run
PYMODULE:=itils

all: check type format lint bandit

check:
	poetry check

type:
	$(CMD) mypy $(PYMODULE)

# No need for `--recursive`:
# https://pycqa.github.io/isort/docs/upgrade_guides/5.0.0/#-recursive-or-rc
isort:
	$(CMD) isort $(PYMODULE)

black:
	$(CMD) black $(PYMODULE)

lint:
	$(CMD) flake8 $(PYMODULE)

bandit:
	$(CMD) bandit -r $(PYMODULE)

format: isort black
