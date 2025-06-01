from agents import Agent, Runner
import sys
import os

# Add the src directory to the path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from agent.settings import settings


def create_obama_agent():
    """Create the Michelle Obama knowledge agent."""
    return Agent(
        name="Michelle Obama Knowledge Assistant",
        instructions="""You are an expert on Michelle Obama, former First Lady, author, and public figure. 
        You can discuss her life, her role as First Lady (2009-2017), her initiatives like Let's Move! and Reach Higher, 
        her books (Becoming, The Light We Carry), her advocacy for education, health, and military families, 
        her background as a lawyer and her work at Princeton and Harvard. 
        Be knowledgeable, respectful, and informative about her accomplishments and impact.""",
        model=settings.model_name,
    )


def interactive_mode():
    """Run the Michelle Obama agent in interactive mode."""
    agent = create_obama_agent()
    
    print("\n👩🏾‍💼 Michelle Obama Knowledge Assistant")
    print("━" * 40)
    print("\n👋 Hello! I'm here to discuss Michelle Obama, former First Lady,")
    print("   her books, initiatives, and remarkable life.")
    print("\n   Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input("💬 You: ").strip()
            
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("\n👋 Thank you for learning about Michelle Obama! Goodbye!")
                break
                
            if not user_input:
                print("Please enter a question about Michelle Obama.\n")
                continue

            # Run the agent with user input
            result = Runner.run_sync(agent, user_input)
            
            # Display the response
            print(f"\n👩🏾‍💼 Michelle Obama Expert: {result.final_output}\n")

        except KeyboardInterrupt:
            print(f"\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}\n")


def main():
    """Run a single example query about Michelle Obama."""
    agent = create_obama_agent()
    
    print("Michelle Obama Knowledge Assistant")
    print("Using model:", settings.model_name)
    print("-" * 40)
    
    result = Runner.run_sync(agent, "What were Michelle Obama's major initiatives as First Lady?")
    print(result.final_output)


if __name__ == "__main__":
    # Check if we want interactive mode
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_mode()
    else:
        main()