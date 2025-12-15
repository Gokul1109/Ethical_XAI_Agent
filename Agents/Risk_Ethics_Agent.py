from langchain_community.llms import Ollama
from config.prompts import risk_ethics_prompt
import json

llm = Ollama(model="llama3", temperature=0)

def run_risk_ethics_agent(task: dict, teams: list) -> str:
    """
    Evaluates ethical risks of project decisions
    and provides multi-perspective justification.
    """
    chain = risk_ethics_prompt | llm

    result = chain.invoke({
        "task": json.dumps(task),
        "teams": json.dumps(teams)
    })

    return result