from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="You are a helpful assistant", model="gpt-4o-2024-11-20")

result = Runner.run_sync(agent, "What were Michelle Obama's favorite books?")
print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.