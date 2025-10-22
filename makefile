# Makefile for Project1 , works for Unix/Linux/macOS and Git Bash on windows

PYTHON ?= python3

.PHONY: version venv install test coverage htmlcov clean all

version:
	@echo "Using Python: $(PYTHON)"
	@which $(PYTHON)
	@$(PYTHON) --version

venv:
	@if [ ! -d "venv" ]; then \
		$(PYTHON) -m venv venv; \
	fi
	@echo "Activate with:"
	@echo "  Windows: venv\\Scripts\\activate"
	@echo "  Unix/macOS: source venv/bin/activate"

install:
	@echo "Installing dependencies..."
	@$(PYTHON) -m pip install --upgrade pip
	@$(PYTHON) -m pip install -r requirements.txt

test:
	@echo "Running unit tests..."
	@$(PYTHON) -m unittest discover -s tests

coverage:
	@echo "Running coverage..."
	@coverage run -m unittest discover -s tests
	@coverage report -m

htmlcov:
	@echo "Generating HTML coverage report..."
	@coverage html
	@echo "Open htmlcov/index.html in your browser"

clean:
	@echo "Cleaning files..."
	@if [ -d "__pycache__" ]; then rm -rf __pycache__; fi
	@if [ -f ".coverage" ]; then rm .coverage; fi
	@if [ -d "htmlcov" ]; then rm -rf htmlcov; fi

.PHONY: lint pylint flake8 install-linters

lint: pylint flake8

pylint:
	@echo "🔍 Running pylint..."
	@pylint bot.py ui.py

flake8:
	@echo "🔍 Running flake8..."
	@flake8 bot.py ui.py

install-linters:
	@echo "Installing linting tools"
	pip install --upgrade pip
	pip install pylint flake8-docstrings flake8-polyfill
	 
