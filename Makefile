SYSTEM_PYTHON=python3.7
VENV:=venv

PIP:=$(VENV)/bin/pip
PYTHON:=$(VENV)/bin/python3
PYTEST:=$(VENV)/bin/pytest

$(VENV):
	$(SYSTEM_PYTHON) -m venv venv

.PHONY: pip-install-dep
pip-install-dep: $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

.PHONY: pip-install-test
pip-install-test: $(VENV)
	$(PIP) install -r requirements-test.txt

.PHONY: pip-install
pip-install: pip-install-dep pip-install-test



.PHONY: test-unit
test-unit:
	$(PYTEST) tests/unit

.PHONY: test-apiclientnodb
test-apiclientnodb:
	$(PYTEST) tests/apiclientnodb

.PHONY: test-apiclientnodb
test-apiclientnodb:
	$(PYTEST) tests/apiclientdb

.PHONY: test-all
test-all: test-unit test-apiclientnodb