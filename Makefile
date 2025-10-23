# Makefile for Project1, works for Unix/Linux/macOS and Git Bash on Windows

PYTHON ?= python3

.PHONY: version venv install test coverage htmlcov clean all lint pylint flake8 install-linters html clean-doc

# Visa aktuell Python-version
version:
	@echo "Using Python: $(PYTHON)"
	@which $(PYTHON)
	@$(PYTHON) --version

# Skapa virtual environment
venv:
	@if [ ! -d "venv" ]; then \
		$(PYTHON) -m venv venv; \
	fi
	@echo "Activate with:"
	@echo "  Windows: venv\\Scripts\\activate"
	@echo "  Unix/macOS: source venv/bin/activate"

# Installera projektberoenden
install:
	@echo "Installing dependencies..."
	@$(PYTHON) -m pip install --upgrade pip
	@$(PYTHON) -m pip install -r requirements.txt

# Kör tester
test:
	@echo "Running unit tests..."
	@$(PYTHON) -m unittest discover -s tests

# Täckningsgrad (coverage)
coverage:
	@echo "Running coverage..."
	@coverage run -m unittest discover -s tests
	@coverage report -m

# Generera HTML-rapport för coverage
htmlcov:
	@echo "Generating HTML coverage report..."
	@coverage html
	@echo "Open htmlcov/index.html in your browser"

# Rensa cache, coverage, rapporter
clean:
	@echo "Cleaning files..."
	@find . -type d -name "__pycache__" -exec rm -r {} +
	@rm -f .coverage
	@rm -rf htmlcov

# 🔍 Lintning (strikt Python-stil)
lint: pylint flake8

pylint:
	@echo "🔍 Running pylint..."
	@pylint bot.py ui.py tests

flake8:
	@echo "🔍 Running flake8..."
	@flake8 bot.py ui.py tests

# Installera linters enligt instruktion: strikt stil, utan förenkling
install-linters:
	@echo "Installing linting tools..."
	@$(PYTHON) -m pip install --upgrade pip
	@$(PYTHON) -m pip install pylint flake8 flake8-docstrings flake8-polyfill

# Bygg Sphinx-dokumentation
html:
	@echo "Building HTML documentation with Sphinx..."
	@sphinx-build -b html doc/source doc/build/html
	@echo "HTML documentation generated in doc/build/html"

# Rensa dokumentationsfiler
clean-doc:
	@echo "Cleaning up Sphinx build directories..."
	@rm -rf doc/build/*
