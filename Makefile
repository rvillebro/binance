#!/usr/bin/make -f
PYTHON	?= python3.9
VENV	?= .venv

.PHONY: install install_test install_doc dev test html latex latexpdf


$(VENV):
	@echo "=== creating virtual environment ==="
	$(PYTHON) -m venv $(VENV)
	@echo "=== updating pip wheel and setuptools ==="
	$(VENV)/bin/pip install --upgrade pip wheel setuptools


install: $(VENV)
	@echo "=== installing src requirements ==="
	$(VENV)/bin/pip install -r requirements.txt


install_doc: install
	@echo "=== installing doc requirements ==="
	$(VENV)/bin/pip install -r doc/requirements.txt


install_test: install
	@echo "=== installing test requirements ==="
	$(VENV)/bin/pip install -r src/tests/requirements.txt


dev: install_doc install_test
	@echo "=== installing binance package as editable ==="
	$(VENV)/bin/pip install -e .


test: install_test
	@echo "=== running test ==="
	pytest src/tests


html latex latexpdf: install_doc
	@echo "=== making $@ documentation ==="
	@cd doc && $(MAKE) $@
