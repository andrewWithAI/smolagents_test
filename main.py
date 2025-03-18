from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

model = HfApiModel()
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

agent.run("Look up the current prices web developers charge in the DFW area, then create a table of price ranges that could be used as a starting point for negotiations?")
