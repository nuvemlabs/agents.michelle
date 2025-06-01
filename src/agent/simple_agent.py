from agents import Agent, Runner
import sys
import os

# Add the src directory to the path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from agent.settings import settings


def create_creative_agent():
    """Create the creative assistant agent."""
    return Agent(
        name="Creative Assistant",
        instructions=settings.agent_default_instructions,
        model=settings.model_name,
    )


def interactive_mode():
    """Run the creative agent in interactive mode."""
    agent = create_creative_agent()
    
    print("\n✨ Creative Assistant")
    print("━" * 30)
    print("\n🎨 Hello! I'm your creative writing assistant.")
    print("   I can help you with poetry, stories, creative writing, and more!")
    print("\n   Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input("💬 You: ").strip()
            
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("\n👋 Thanks for being creative with me! Goodbye!")
                break
                
            if not user_input:
                print("Please enter a request.\n")
                continue

            # Run the agent with user input
            result = Runner.run_sync(agent, user_input)
            
            # Display the response
            print(f"\n✨ Creative Assistant: {result.final_output}\n")

        except KeyboardInterrupt:
            print(f"\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}\n")


def main():
    """Run a simple agent with Pydantic configuration."""
    
    # Create agent using settings
    agent = create_creative_agent()

    # Use the default creative task from settings
    task = settings.creative_config.default_task
    
    print(f"Running task: {task}")
    print(f"Using model: {settings.model_name}")
    print(f"Temperature: {settings.model_temperature}")
    print("-" * 50)
    
    result = Runner.run_sync(agent, task)
    print(result.final_output)


if __name__ == "__main__":
    # Check if we want interactive mode
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_mode()
    else:
        main() 