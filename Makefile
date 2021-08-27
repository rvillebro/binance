#!/usr/bin/make -f
PYTHON	?= python3.9
VENV	?= .venv

.PHONY: install_binance install_test install_doc dev test html latex latexpdf


$(VENV):
	@echo "=== creating virtual environment ==="
	$(PYTHON) -m venv $(VENV)
	@echo "=== updating pip wheel and setuptools ==="
	$(VENV)/bin/pip install --upgrade pip wheel setuptools


install_binance: $(VENV)
	@echo "=== installing binance package as editable ==="
	$(VENV)/bin/pip install -e .


install_test: install_binance
	@echo "=== installing test requirements ==="
	$(VENV)/bin/pip install -r src/tests/requirements.txt


install_doc: install_binance
	@echo "=== installing doc requirements ==="
	$(VENV)/bin/pip install -r doc/requirements.txt


dev: install_test install_doc 


test: install_test
	@echo "=== running test ==="
	pytest src/tests


html latex latexpdf: install_doc
	@echo "=== making $@ documentation ==="
	@cd doc && $(MAKE) $@


clean:
	@echo "=== cleaning documentation ==="
	@cd doc && $(MAKE) clean
	@echo "=== removing $(VENV) ==="
	rm -rf $(VENV)
