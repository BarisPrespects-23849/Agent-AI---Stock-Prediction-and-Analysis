from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo

# Define the agent
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    description="You are a senior NYT researcher tasked with searching for and summarizing information on a topic.",
    instructions=[
        "Search for the top 5 relevant links on the given topic using DuckDuckGo.",
        "Extract the article text from each URL. If a URL is unavailable or does not contain usable content, skip it.",
        "Summarize the content to create an NYT-worthy article based on the retrieved information.",
    ],
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
)

# Perform a search and generate the response
topic = "Simulation theory"  # Replace this with any topic you want to search
response = agent.print_response(topic, stream=True)

# Print the final response
print(response)
