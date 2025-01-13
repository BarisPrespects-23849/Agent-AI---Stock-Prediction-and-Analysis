from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools

# Define the agent
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools()],
    description="You are a financial analyst tasked with analyzing and predicting the long-term performance of Indian mutual funds.",
    instructions=[
        "Retrieve data for the following mutual funds over the last 5 years:",
        "- Parag Parikh Flexi Cap Fund",
        "- Motilal Oswal Midcap Fund",
        "- Nippon India Small Cap Fund",
        "- Quant Active Fund",
        "- Motilal Oswal Small Cap Fund.",
        "Analyze long-term trends such as NAV growth, market cycles, expense ratios, and sector allocations.",
        "Consider macroeconomic factors, historical performance, and long-term market conditions in your prediction.",
        "Provide long-term predictions for the next 4-5 years based on historical data, expected market growth, and economic trends.",
        "Summarize your predictions into a comprehensive report, including potential risks, market volatility, and long-term benefits of investing in these funds.",
    ],
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
)

# Perform the task and generate the response
response = agent.print_response("Long-term predictions (4-5 years) for multiple Indian mutual funds", stream=True)

# Print the final response
print(response)
