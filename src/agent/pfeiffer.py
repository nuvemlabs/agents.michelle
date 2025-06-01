from agents import Agent, Runner
import asyncio
import sys
import os

# Add the src directory to the path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from agent.settings import settings

# Create agents using Pydantic configuration
spanish_config = settings.get_agent_config("spanish_agent")
spanish_agent = Agent(
    name=spanish_config.name,
    instructions=spanish_config.instructions,
    model=settings.model_name,
)

english_config = settings.get_agent_config("english_agent")
english_agent = Agent(
    name=english_config.name,
    instructions=english_config.instructions,
    model=settings.model_name,
)

triage_config = settings.get_agent_config("triage_agent")
triage_agent = Agent(
    name=triage_config.name,
    instructions=triage_config.instructions,
    model=settings.model_name,
    handoffs=[spanish_agent, english_agent],
)


async def main():
    result = await Runner.run(triage_agent, input="Hola, ¿cómo estás?")
    print(result.final_output)
    # ¡Hola! Estoy bien, gracias por preguntar. ¿Y tú, cómo estás?


if __name__ == "__main__":
    asyncio.run(main())