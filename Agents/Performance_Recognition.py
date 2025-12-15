from langchain_community.llms import Ollama
from config.prompts import performance_review_prompt
import json

llm = Ollama(model="llama3")

def run_performance_review_agent(task: dict, users: list) -> str:
    """
    Performance Review Agent.

    Uses existing task difficulty and user workload
    as proxies for contribution and complexity.
    """
    chain = performance_review_prompt | llm

    result = chain.invoke({
        "task": json.dumps(task),
        "users": json.dumps(users)
    })

    return result