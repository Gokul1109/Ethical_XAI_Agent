from langchain_community.llms import Ollama
from config.prompts import ethical_prompt
import json

llm = Ollama(model="llama3")

def run_ethical_agent(task: dict, users: list) -> str:
    """
    Takes a task dict and list of user dicts.
    Returns a STRING with JSON inside (from the OPENAI Model).
    """
    chain = ethical_prompt | llm

    result = chain.invoke({
        "task": json.dumps(task),
        "users": json.dumps(users)
    })

    # Final result of ethical decisions
    return result