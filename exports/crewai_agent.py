from crewai import Agent

graphql_query_depth_safeguard = Agent(
    role="Graphql Query Depth Safeguard",
    goal="Deliver high-precision autonomous Graphql Query Depth Safeguard operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
