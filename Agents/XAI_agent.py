from langchain_community.llms import Ollama
from config.prompts import explain_prompt
import json

llm = Ollama(model="llama3")


def run_explainable_agent(decision_json_str: str) -> str:
    """
    Takes the JSON string produced by the ethical agent.
    Returns a natural-language explanation string.
    """
    chain = explain_prompt | llm

    result = chain.invoke({
        "decision": decision_json_str
    })

    return result

