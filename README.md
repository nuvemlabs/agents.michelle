# agents.michelle 🎭

An AI agent system featuring **Michelle Pfeiffer** as the main agent with her director friends **Tim Burton** and **Martin Scorsese**. This project demonstrates OpenAI's agents SDK handoff functionality in an engaging Hollywood context.

## 🌟 Features

- **🎭 Michelle Pfeiffer Agent System** - Interactive conversations with automatic handoffs
- **🎨 Tim Burton** - Gothic filmmaker personality (Batman Returns collaboration)
- **🎬 Martin Scorsese** - Cinema master personality (The Age of Innocence collaboration)
- **Automatic Handoffs** - Smart routing based on conversation topics
- **Interactive Mode** - Continuous conversations with context preservation
- **Creative Agents** - Poetry, storytelling, and creative writing assistants
- **Pydantic Configuration** - Type-safe, environment-based settings

## 🎬 The Cast

### Michelle Pfeiffer (Main Agent) 🎭
The elegant, accomplished actress who can discuss her career, acting techniques, and collaborations. She intelligently hands off conversations to her director friends when appropriate.

### Tim Burton 🎨
The gothic visionary director. When you ask about **Batman Returns**, **Catwoman**, or **gothic filmmaking**, Michelle hands you off to Tim for his unique perspective.

### Martin Scorsese 🎬
The passionate cinema historian. Questions about **The Age of Innocence**, **method acting**, or **period films** get routed to Martin for his deep insights.

## 🚀 Quick Start

### 1. Setup
```bash
cd projects/agents.michelle
source env/bin/activate  # Virtual environment already configured
export OPENAI_API_KEY="your-api-key-here"
```

### 2. Try the Michelle Pfeiffer System
```bash
# Single interaction example
make pfeiffer

# Interactive conversation mode  
make interactive

# Test handoff functionality
make test-handoffs
```

### 3. Other Agents
```bash
make simple     # Creative writing assistant
make obama      # Michelle Obama knowledge agent
make run-all    # Try everything
```

## 🎯 Usage Examples

### Interactive Michelle Pfeiffer System
```bash
make interactive
```
🎭 Michelle Pfeiffer Agent System
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👋 Hello! I'm Michelle Pfeiffer. I'm here to chat about my career,
   my films, and the wonderful directors I've worked with.

   I can handoff our conversation to:
   🎨 Tim Burton (Batman Returns director)
   🎬 Martin Scorsese (The Age of Innocence director)

💬 You: Tell me about Batman Returns
🎨 Tim Burton: Ah, Batman Returns—what a wonderfully dark playground...
```

### Sample Conversations
- **"Tell me about Batman Returns"** → Handoff to Tim Burton
- **"What about The Age of Innocence?"** → Handoff to Martin Scorsese  
- **"How do you approach character development?"** → Stays with Michelle
- **"What's your favorite acting technique?"** → Michelle discusses her craft

## 🛠️ Makefile Commands

### 🎭 Main Agent System
```bash
make pfeiffer           # Run Michelle Pfeiffer system (single interaction)
make interactive        # Interactive conversation mode
make pfeiffer-interactive # Alias for interactive mode
make test-handoffs      # Test the handoff functionality
```

### 🤖 Other Agents
```bash
make simple             # Creative assistant agent
make obama              # Michelle Obama knowledge agent  
make run-all            # Run all agents sequentially
```

### 🔧 Development & Testing
```bash
make check-config       # Validate configuration files
make test-api          # Test OpenAI API connection
make list-models       # Show available models
make status            # Project status and info
```

### 🎨 Interactive Features
```bash
make demo              # Full demo of all agents
make shell             # Python shell with agents loaded
make creative          # Custom creative writing task
```

### 🧹 Maintenance
```bash
make setup             # Set up virtual environment
make clean             # Clean cache and temp files
make update            # Update dependencies
make help              # Show all commands
```

## 🔧 Configuration

The project uses a Pydantic-based configuration system with emoji support:

### `config/settings.yaml`
```yaml
# Model Configuration
model:
  name: gpt-4o-2024-11-20
  temperature: 0.7
  max_tokens: 2000

# Agent Configuration for Michelle Pfeiffer System
agents:
  michelle:
    name: "Michelle Pfeiffer"
    emoji: "🎭"
    instructions: |
      You are Michelle Pfeiffer, the accomplished actress...
      When users ask about Batman Returns, you can handoff to Tim Burton...
      
  tim_burton:
    name: "Tim Burton"  
    emoji: "🎨"
    instructions: |
      You are Tim Burton, the visionary director...
      
  martin_scorsese:
    name: "Martin Scorsese"
    emoji: "🎬" 
    instructions: |
      You are Martin Scorsese, the master filmmaker...
```

### Environment Variables
```bash
export OPENAI_API_KEY="your-key"
export MODEL_NAME="gpt-4o-2024-11-20"  # Optional override
export MODEL_TEMPERATURE="0.7"         # Optional override
```

## 📁 Project Structure

```
agents.michelle/
├── config/
│   └── settings.yaml          # Agent configurations with emojis
├── src/agent/
│   ├── settings.py           # Pydantic configuration classes
│   ├── pfeiffer.py           # Michelle Pfeiffer agent system ⭐
│   ├── simple_agent.py       # Creative writing assistant
│   └── obama.py              # Michelle Obama knowledge agent
├── tests/
│   ├── test_agents.py        # Individual agent tests
│   ├── test_handoffs.py      # Handoff functionality tests
│   └── test_interactive.py   # Interactive mode tests
├── Makefile                  # Project automation (22 targets)
├── README.md                 # This file
└── AGENT_DESIGN_PLAN.md     # Detailed system design
```

## 🧪 Testing

### Automated Tests
```bash
make test              # Run all tests
make test-handoffs     # Test agent handoff functionality
make test-interactive  # Test interactive modes
```

### Manual Testing
```bash
# Test Michelle → Tim Burton handoff
echo "Tell me about Batman Returns" | make interactive

# Test Michelle → Martin Scorsese handoff  
echo "Tell me about The Age of Innocence" | make interactive

# Test general conversation stays with Michelle
echo "What's your favorite acting method?" | make interactive
```

## 🎨 Interactive Modes

All agents now support interactive mode with the `--interactive` flag:

### Michelle Pfeiffer System
```bash
python src/agent/pfeiffer.py --interactive
```

### Creative Assistant
```bash
python src/agent/simple_agent.py --interactive
```

### Michelle Obama Agent
```bash
python src/agent/obama.py --interactive
```

## 🐛 Troubleshooting

### Model Access Issues
The project is configured to use `gpt-4o-2024-11-20`. If you encounter access issues:

```bash
make list-models        # Check available models
make test-api          # Test API connection
```

### Handoff Not Working
If agents aren't handing off correctly:

```bash
make test-handoffs     # Run handoff tests
make check-config      # Validate configuration
```

### Common Solutions
- Ensure `OPENAI_API_KEY` is set
- Try different model: edit `config/settings.yaml`
- Check model access: `make list-models`
- Verify configuration: `make check-config`

## 🎯 How Handoffs Work

The system uses OpenAI's agents SDK built-in handoff functionality:

```python
# Michelle Pfeiffer (main agent) with handoffs
michelle_agent = Agent(
    name="Michelle Pfeiffer",
    instructions="You are Michelle Pfeiffer...",
    model=settings.model_name,
    handoffs=[tim_burton_agent, martin_scorsese_agent],  # Magic happens here!
)
```

When Michelle detects questions about:
- **Batman Returns, Catwoman, gothic films** → Hands off to Tim Burton
- **The Age of Innocence, method acting, period films** → Hands off to Martin Scorsese
- **General acting, career questions** → Stays with Michelle

## 🌟 Example Outputs

### Tim Burton Response (Batman Returns)
> "Ah, Batman Returns—what a wonderfully dark playground that was to create in! Working on that film was like being unleashed to construct a strange, gothic snow globe, and Michelle Pfeiffer as Catwoman was absolutely at the heart of it all..."

### Martin Scorsese Response (Age of Innocence)
> "Ah, *The Age of Innocence*. That project is very dear to me. It's a love story, yes, but it's also a story about repression, appearances, and the cage of societal expectation. Edith Wharton's novel—it's just exquisite..."

### Michelle Pfeiffer Response (General)
> "You know, after all these years in the business, I've learned that every role teaches you something new about yourself and about the craft..."

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch  
3. Add tests for new functionality
4. Ensure all tests pass: `make test`
5. Update documentation
6. Submit a pull request

## 📄 License

This project is licensed under the terms specified in the LICENSE file.

## 🆘 Support

For issues or questions:
1. Check this README and troubleshooting section
2. Run `make status` to check configuration
3. Use `make test-handoffs` to verify functionality
4. Review `AGENT_DESIGN_PLAN.md` for system design details

---

**✨ Built with OpenAI's agents SDK handoff functionality - Simple, elegant, and powerful!**
