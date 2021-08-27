PYTHON	?= python3.9
VENV	?= .venv


$(VENV):
	@echo "=== creating virtual environment ==="
	@$(PYTHON) -m venv $(VENV)
	@echo "=== updating pip wheel and setuptools ==="
	@$(VENV)/bin/pip install --upgrade pip wheel setuptools


.PHONY: install

install: $(VENV)
	@echo "=== installing src requirements ==="
	@$(VENV)/bin/pip install -r requirements.txt


.PHONY: install_docs

install_docs: install
	@echo "=== installing docs requirements ==="
	@$(VENV)/bin/pip install -r docs/requirements.txt
