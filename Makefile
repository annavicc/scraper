define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("	%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

PIP := pip install -r
PROJECT_NAME := xpert
PYTHON_VERSION := 3.8.0

.DEFAULT: help
.PHONY: help deps all

help: ## List all available commands
	@echo "Usage: make <command> \n"
	@echo "options:"
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

.pip:
	pip install pip --upgrade

install: .pip  ## Install all requirements required for local development
	$(PIP) requirements.txt

run: ## Run aplication
	scrapy crawl categories
