ENV_DIR=.env

ifeq ($(OS),Windows_NT)
	IN_ENV=. $(ENV_DIR)/Scripts/activate &&
else
	IN_ENV=. $(ENV_DIR)/bin/activate &&
endif

all: test lint docs artifacts

env: $(ENV_DIR)

test: build plain-test

plain-test:
	$(IN_ENV) tox -p all

artifacts: build_reqs sdist

$(ENV_DIR):
	virtualenv $(ENV_DIR)

build_reqs: env
	$(IN_ENV) pip install sphinx tox coverage

build: build_reqs
	$(IN_ENV) pip install --editable .

sdist: build_reqs
	$(IN_ENV) python setup.py sdist

lint: build plain-lint

plain-lint:
	$(IN_ENV) tox -e codestyle

docs: build_reqs
	$(IN_ENV) pip install -r docs/requirements.txt
	$(IN_ENV) $(MAKE) -C docs html

freeze: env
	- $(IN_ENV) pip freeze

clean:
	- @rm -rf docs/build
	- @rm -rf src/*.egg-info
	- @rm -f .coverage
	- @rm -f test_results.xml
	- @rm -f coverage.xml
	- @rm -rf .tox
	- @find ./src ./docs -name '*.pyc' | xargs -r rm

env_clean: clean
	- @rm -rf $(ENV_DIR)
