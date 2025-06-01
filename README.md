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

## 🎯 Usage

### Basic Usage
Run the main agent script:

```bash
python src/agent/agent.py
```

### Expected Output
The script will generate a haiku about recursion in programming. Example output:
```
Code calls itself back,  
Infinite loops or returns—  
Logic spins in time.
```

## 🔧 Configuration

### Model Selection
The agent is configured to use `gpt-4o-2024-11-20`. If you need to use a different model, modify the `model` parameter in `src/agent/agent.py`:

```python
agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant", 
    model="gpt-4o-2024-11-20"  # Change this to your preferred model
)
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
├── env/                    # Virtual environment
├── src/
│   └── agent/
│       └── agent.py       # Main agent script
├── workflow_state.md      # Development workflow tracking
├── README.md             # This file
├── .gitignore           # Git ignore rules
└── LICENSE              # Project license
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
