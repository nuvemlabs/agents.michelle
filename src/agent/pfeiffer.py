from agents import Agent, Runner
import asyncio
import sys
import os

# Add the src directory to the path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from agent.settings import settings

# Create Tim Burton agent
tim_config = settings.get_agent_config("tim_burton")
tim_burton_agent = Agent(
    name=tim_config.name,
    instructions=tim_config.instructions,
    model=settings.model_name,
)

# Create Martin Scorsese agent
martin_config = settings.get_agent_config("martin_scorsese")
martin_scorsese_agent = Agent(
    name=martin_config.name,
    instructions=martin_config.instructions,
    model=settings.model_name,
)

# Create Michelle Pfeiffer agent with handoffs to her director friends
michelle_config = settings.get_agent_config("michelle")
michelle_agent = Agent(
    name=michelle_config.name,
    instructions=michelle_config.instructions,
    model=settings.model_name,
    handoffs=[tim_burton_agent, martin_scorsese_agent],
)


def interactive_mode():
    """Run the agent in interactive mode."""
    print(f"\n{michelle_config.emoji} {michelle_config.name} Agent System")
    print("━" * 50)
    print(f"\n👋 Hello! I'm {michelle_config.name}. I'm here to chat about my career,")
    print("   my films, and the wonderful directors I've worked with.")
    print(f"\n   I can handoff our conversation to:")
    print(f"   {tim_config.emoji} {tim_config.name} (Batman Returns director)")
    print(f"   {martin_config.emoji} {martin_config.name} (The Age of Innocence director)")
    print("\n   Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input("💬 You: ").strip()
            
            if user_input.lower() in ["exit", "quit", "bye"]:
                print(f"\n👋 Thank you for chatting with me! Goodbye!")
                break
                
            if not user_input:
                print("Please enter a message.\n")
                continue

            # Run the agent with user input
            result = Runner.run_sync(michelle_agent, user_input)
            
            # Display the response
            print(f"\n🎭 Response: {result.final_output}\n")

        except KeyboardInterrupt:
            print(f"\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}\n")


async def main():
    """Example of a single interaction."""
    result = await Runner.run(michelle_agent, input="Tell me about working with Tim Burton on Batman Returns.")
    print(f"\n{michelle_config.emoji} {result.final_output}")


if __name__ == "__main__":
    # Check if we want interactive mode
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_mode()
    else:
        asyncio.run(main())