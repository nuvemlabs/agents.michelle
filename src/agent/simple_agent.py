from agents import Agent, Runner
import sys
import os

# Add the src directory to the path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from agent.settings import settings

def main():
    """Run a simple agent with Pydantic configuration."""
    
    # Create agent using settings
    agent = Agent(
        name="Creative Assistant",
        instructions=settings.agent_default_instructions,
        model=settings.model_name,
    )

    # Use the default creative task from settings
    task = settings.creative_config.default_task
    
    print(f"Running task: {task}")
    print(f"Using model: {settings.model_name}")
    print(f"Temperature: {settings.model_temperature}")
    print("-" * 50)
    
    result = Runner.run_sync(agent, task)
    print(result.final_output)

if __name__ == "__main__":
    main() 