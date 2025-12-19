"""
Azure Bot using Azure AI Projects Agent
"""
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Azure AI Project endpoint
myEndpoint = "https://foundarydec251219.services.ai.azure.com/api/projects/proj-default"

# Initialize the AI Project Client with DefaultAzureCredential
project_client = AIProjectClient(
    endpoint=myEndpoint,
    credential=DefaultAzureCredential(),
)

# Agent name
myAgent = "bot"

# Get an existing agent
agent = project_client.agents.get_agent(myAgent)

print(f"Successfully retrieved agent: {agent.name}")
print(f"Agent ID: {agent.id}")
print(f"Agent description: {agent.description}")
