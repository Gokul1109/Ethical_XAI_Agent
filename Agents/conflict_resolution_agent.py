from langchain_community.llms import Ollama
from config.prompts import conflict_resolution_prompt
import json

llm = Ollama(model="llama3")

def run_conflict_resolution_agent(task: dict, teams: list, users: list) -> str:
    """
    Resolves conflicts between speed, quality, and team well-being
    across multiple teams using a shared project dataset.
    """
    chain = conflict_resolution_prompt | llm

    result = chain.invoke({
        "task": json.dumps(task),
        "teams": json.dumps(teams),
        "users": json.dumps(users)
    })

    return result