# agents.michelle

A simple AI agent implementation using OpenAI's GPT models. This project demonstrates how to create and run an AI assistant that can generate creative content like haikus about programming concepts.

## 🚀 Features

- Simple AI agent implementation using the `agents` library
- OpenAI GPT model integration
- Creative text generation (poetry, haikus, etc.)
- Virtual environment setup for clean dependency management

## 📋 Prerequisites

- Python 3.13.3 (or compatible version)
- OpenAI API key
- Access to OpenAI GPT models

## 🛠️ Setup

### 1. Clone and Navigate
```bash
cd projects/agents.michelle
```

### 2. Virtual Environment
The project includes a pre-configured virtual environment in the `env/` directory:

```bash
# Activate the virtual environment
source env/bin/activate
```

### 3. Environment Variables
Ensure your OpenAI API key is set:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

### 4. Dependencies
The required dependencies should already be installed in the virtual environment:
- `agents` - The main agent framework
- `openai` - OpenAI API client
- `pydantic` - Data validation and settings management
- `pydantic-settings` - Environment-based settings
- `PyYAML` - YAML configuration file support

If you need to reinstall dependencies:
```bash
pip install agents openai pydantic pydantic-settings PyYAML
```

## 🛠️ Makefile Features

The project includes a comprehensive Makefile with the following categories of targets:

### Agent Execution
- `make simple` - Run the creative assistant agent
- `make pfeiffer` - Run the multi-language agent system  
- `make obama` - Run the Obama knowledge agent
- `make run-all` / `make all` - Run all agents sequentially

### Configuration & Testing  
- `make check-config` - Validate configuration files
- `make list-models` - List available OpenAI models
- `make test-api` - Test OpenAI API connection
- `make status` - Show project status and configuration

### Development & Maintenance
- `make setup` / `make install` - Set up virtual environment
- `make clean` - Clean cache and temporary files
- `make update` - Update all dependencies
- `make requirements` - Generate requirements.txt

### Interactive Features
- `make demo` - Run a full demo of all agents
- `make shell` - Start Python shell with settings loaded
- `make creative` - Run custom creative task
- `make spanish` - Test Spanish language agent specifically

### Help
- `make help` - Show all available targets (default)

## 🎯 Usage

### Quick Start with Makefile
This project includes a comprehensive Makefile for easy management:

```bash
# Show all available commands
make help

# Run all agents sequentially  
make run-all

# Run individual agents
make simple      # Creative assistant
make pfeiffer    # Multi-language system
make obama       # Obama knowledge agent

# Project management
make status      # Show project status
make check-config # Validate configuration
```

### Manual Usage
You can also run agents directly:

```bash
python src/agent/simple_agent.py
python src/agent/pfeiffer.py
python src/agent/obama.py
```

### Expected Output
The script will generate a haiku about recursion in programming. Example output:
```
Code calls itself back,  
Infinite loops or returns—  
Logic spins in time.
```

## 🔧 Configuration

### Pydantic Configuration System
The project uses a Pydantic-based configuration system similar to agents.tracie for better maintainability and validation.

#### Configuration Files
- `config/settings.yaml` - Main configuration file
- `src/agent/settings.py` - Pydantic settings classes

#### Model Selection
You can configure the model in `config/settings.yaml`:

```yaml
model:
  name: gpt-4o-2024-11-20     # Working model for this project
  temperature: 0.7            # Creative responses for haikus/poetry
  max_tokens: 2000            # Reasonable limit for creative tasks
```

Or override via environment variables:
```bash
export MODEL_NAME="gpt-4"
export MODEL_TEMPERATURE="0.5"
```

### Available Models
To check which models are available with your API key:

```python
import openai
client = openai.OpenAI()
models = client.models.list()
available_models = [m.id for m in models.data if 'gpt' in m.id]
print(available_models)
```

## 📁 Project Structure

```
agents.michelle/
├── config/
│   └── settings.yaml      # Configuration file
├── env/                   # Virtual environment
├── src/
│   └── agent/
│       ├── settings.py    # Pydantic settings classes
│       ├── simple_agent.py # Simple agent with configuration
│       ├── pfeiffer.py    # Multi-language agent system
│       └── obama.py       # Obama knowledge agent
├── Makefile              # Project automation and management
├── workflow_state.md     # Development workflow tracking
├── README.md            # This file
├── .gitignore          # Git ignore rules
└── LICENSE             # Project license
```

## 🐛 Troubleshooting

### Model Access Issues
If you encounter "model not found" errors:

1. **Check Available Models**: Use the model checking script above
2. **Update Model Name**: Use the exact model ID from your available models list
3. **API Key Permissions**: Ensure your API key has access to the desired models

### Common Error: `Project does not have access to model`
This means your OpenAI project doesn't have access to the specific model version. Try using:
- `gpt-4o-2024-11-20`
- `gpt-4`
- `chatgpt-4o-latest`

### Virtual Environment Issues
If the virtual environment doesn't work:

```bash
# Create a new virtual environment
python3.13 -m venv env
source env/bin/activate
pip install agents openai
```

## 💡 Customization

### Changing the Task
Modify the task in `src/agent/agent.py`:

```python
result = Runner.run_sync(agent, "Your custom prompt here")
```

### Modifying Agent Instructions
Update the agent's behavior:

```python
agent = Agent(
    name="Assistant", 
    instructions="Your custom instructions here",
    model="gpt-4o-2024-11-20"
)
```

## 📝 Example Variations

### Different Creative Tasks
```python
# Generate a limerick about coding
result = Runner.run_sync(agent, "Write a limerick about debugging code.")

# Explain a concept
result = Runner.run_sync(agent, "Explain machine learning in simple terms.")

# Code generation
result = Runner.run_sync(agent, "Write a Python function to calculate fibonacci numbers.")
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the terms specified in the LICENSE file.

## 🆘 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify your OpenAI API key and model access
3. Ensure all dependencies are properly installed
4. Review the workflow_state.md for development notes

---

**Note**: This project was successfully tested with Python 3.13.3 and OpenAI's gpt-4o-2024-11-20 model.
