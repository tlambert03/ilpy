.PHONY: default install-dev tests clean docs docs-watch

default:
	pip install .

install-dev:
	pip install -e .[dev]

tests:
	pytest -v --cov=ilpy --cov-report=term-missing
	pre-commit run --all-files

clean:
	rm -rf build dist
	rm -rf ilpy/*.cpp
	rm -rf ilpy/*.so

docs:
	make -C docs html

docs-watch:
	pip install sphinx-autobuild
	sphinx-autobuild docs/source docs/_build/html
