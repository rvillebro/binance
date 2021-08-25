PYTHON	?= python3.9
VENV	?= .venv

.PHONY: install

install:
	@echo "=== creating virtual environment ==="
	@$(PYTHON) -m venv $(VENV)
	@echo "=== updating pip wheel and setuptools ==="
	@$(VENV)/bin/pip install --upgrade pip wheel setuptools
	@echo "=== installing requirements ==="
	@$(VENV)/bin/pip install -r requirements.txt
