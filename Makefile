# Makefile for agents.michelle
# This Makefile provides convenient targets to run all agents and manage the project

# Variables
VENV_DIR = env
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip
SRC_DIR = src/agent
CONFIG_DIR = config

# Colors for output
GREEN = \033[0;32m
YELLOW = \033[0;33m
RED = \033[0;31m
NC = \033[0m # No Color

# Default target
.PHONY: help
help: ## Show this help message
	@echo "$(GREEN)agents.michelle - AI Agent Management$(NC)"
	@echo ""
	@echo "$(YELLOW)Available targets:$(NC)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# Setup and installation targets
.PHONY: setup
setup: ## Set up the virtual environment and install dependencies
	@echo "$(GREEN)Setting up virtual environment...$(NC)"
	python3.13 -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install agents openai pydantic pydantic-settings PyYAML
	@echo "$(GREEN)Setup complete!$(NC)"

.PHONY: install
install: setup ## Alias for setup

.PHONY: deps
deps: ## Install/update dependencies
	@echo "$(GREEN)Installing dependencies...$(NC)"
	$(PIP) install --upgrade agents openai pydantic pydantic-settings PyYAML

# Agent execution targets
.PHONY: simple
simple: ## Run the simple agent with configuration
	@echo "$(GREEN)Running simple agent...$(NC)"
	@echo "$(YELLOW)========================================$(NC)"
	$(PYTHON) $(SRC_DIR)/simple_agent.py
	@echo "$(YELLOW)========================================$(NC)"

.PHONY: pfeiffer
pfeiffer: ## Run the multi-language Pfeiffer agent system
	@echo "$(GREEN)Running Pfeiffer multi-language agent...$(NC)"
	@echo "$(YELLOW)========================================$(NC)"
	$(PYTHON) $(SRC_DIR)/pfeiffer.py
	@echo "$(YELLOW)========================================$(NC)"

.PHONY: obama
obama: ## Run the Obama agent
	@echo "$(GREEN)Running Obama agent...$(NC)"
	@echo "$(YELLOW)========================================$(NC)"
	$(PYTHON) $(SRC_DIR)/obama.py
	@echo "$(YELLOW)========================================$(NC)"

# Run all agents
.PHONY: run-all
run-all: simple pfeiffer obama ## Run all agents sequentially
	@echo "$(GREEN)All agents completed!$(NC)"

.PHONY: all
all: run-all ## Alias for run-all

# Configuration and testing targets
.PHONY: check-config
check-config: ## Validate the configuration files
	@echo "$(GREEN)Checking configuration...$(NC)"
	$(PYTHON) -c "import sys; sys.path.append('src'); from agent.settings import settings; print('✓ Configuration loaded successfully'); print(f'Model: {settings.model_name}'); print(f'Task: {settings.creative_config.default_task}')"

.PHONY: list-models
list-models: ## List available OpenAI models
	@echo "$(GREEN)Checking available OpenAI models...$(NC)"
	$(PYTHON) -c "import openai; client = openai.OpenAI(); models = client.models.list(); gpt_models = [m.id for m in models.data if 'gpt' in m.id]; print('Available GPT models:'); [print(f'  - {model}') for model in sorted(gpt_models)]"

.PHONY: test-api
test-api: ## Test OpenAI API connection
	@echo "$(GREEN)Testing OpenAI API connection...$(NC)"
	$(PYTHON) -c "import openai; client = openai.OpenAI(); client.models.list(); print('✓ OpenAI API connection successful')"

# Development targets
.PHONY: clean
clean: ## Clean up cache and temporary files
	@echo "$(GREEN)Cleaning up...$(NC)"
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	find . -type f -name ".DS_Store" -delete 2>/dev/null || true

.PHONY: clean-all
clean-all: clean ## Clean everything including virtual environment
	@echo "$(GREEN)Removing virtual environment...$(NC)"
	rm -rf $(VENV_DIR)

# Interactive targets
.PHONY: shell
shell: ## Start Python shell with environment loaded
	@echo "$(GREEN)Starting Python shell with settings loaded...$(NC)"
	$(PYTHON) -c "import sys; sys.path.append('src'); from agent.settings import settings; print(f'Settings loaded. Model: {settings.model_name}'); import code; code.interact(local=locals())"

.PHONY: demo
demo: ## Run a quick demo of all agents
	@echo "$(GREEN)🤖 Welcome to agents.michelle Demo!$(NC)"
	@echo ""
	@echo "$(YELLOW)Current Configuration:$(NC)"
	@$(MAKE) check-config
	@echo ""
	@echo "$(YELLOW)Running demo of all agents...$(NC)"
	@echo ""
	@$(MAKE) run-all

# Environment and status targets
.PHONY: status
status: ## Show project status and configuration
	@echo "$(GREEN)agents.michelle Project Status$(NC)"
	@echo "=============================="
	@echo "Virtual Environment: $(VENV_DIR)"
	@echo "Python Path: $(PYTHON)"
	@echo ""
	@echo "$(YELLOW)Configuration:$(NC)"
	@$(MAKE) check-config
	@echo ""
	@echo "$(YELLOW)Available Agents:$(NC)"
	@echo "  - simple_agent.py (Creative Assistant)"
	@echo "  - pfeiffer.py (Multi-language Agent System)"
	@echo "  - obama.py (Obama Knowledge Agent)"

.PHONY: env-check
env-check: ## Check if virtual environment is properly set up
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "$(RED)Virtual environment not found. Run 'make setup' first.$(NC)"; \
		exit 1; \
	fi
	@if [ ! -f "$(PYTHON)" ]; then \
		echo "$(RED)Python executable not found in virtual environment.$(NC)"; \
		exit 1; \
	fi
	@echo "$(GREEN)✓ Virtual environment is properly set up$(NC)"

# Custom tasks
.PHONY: creative
creative: ## Run simple agent with a custom creative task
	@echo "$(GREEN)Running creative task...$(NC)"
	@echo "$(YELLOW)========================================$(NC)"
	$(PYTHON) -c "import sys; sys.path.append('src'); from agent.settings import settings; from agents import Agent, Runner; agent = Agent(name='Creative Assistant', instructions=settings.agent_default_instructions, model=settings.model_name); result = Runner.run_sync(agent, 'Write a haiku about artificial intelligence and creativity'); print(result.final_output)"
	@echo "$(YELLOW)========================================$(NC)"

.PHONY: spanish
spanish: ## Test Spanish language agent specifically
	@echo "$(GREEN)Testing Spanish agent...$(NC)"
	@echo "$(YELLOW)========================================$(NC)"
	$(PYTHON) -c "import sys; sys.path.append('src'); from agent.settings import settings; from agents import Agent, Runner; config = settings.get_agent_config('spanish_agent'); agent = Agent(name=config.name, instructions=config.instructions, model=settings.model_name); result = Runner.run_sync(agent, '¿Puedes escribir un poema corto sobre la tecnología?'); print(result.final_output)"
	@echo "$(YELLOW)========================================$(NC)"

# Maintenance targets
.PHONY: update
update: ## Update all dependencies
	@echo "$(GREEN)Updating dependencies...$(NC)"
	$(PIP) install --upgrade pip
	$(PIP) install --upgrade agents openai pydantic pydantic-settings PyYAML

.PHONY: requirements
requirements: ## Generate requirements.txt
	@echo "$(GREEN)Generating requirements.txt...$(NC)"
	$(PIP) freeze > requirements.txt
	@echo "$(GREEN)requirements.txt generated!$(NC)"

# Default goal
.DEFAULT_GOAL := help 