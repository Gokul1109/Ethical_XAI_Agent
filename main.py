import json


from Agents.Ethical_agent import run_ethical_agent
from Agents.XAI_agent import run_explainable_agent
from Agents.Performance_Recognition import run_performance_review_agent
from Agents.conflict_resolution_agent import run_conflict_resolution_agent
from Agents.Risk_Ethics_Agent import run_risk_ethics_agent

def main():
    with open("data/data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    task=data['task']
    users=data['users']
    teams=data['teams']
    print("Loaded task and users from JSON.")

    # 3. Run Ethical Agent
    print("\n Running Ethical Agent...")
    decision_json_str = run_ethical_agent(task, users)
    print("\n--- ETHICAL AGENT DECISION (raw JSON string) ---")
    print(decision_json_str)

    # 4. Run Explainable Agent
    print("\n Running XAI Agent...")
    explanation = run_explainable_agent(decision_json_str)
    print("\n--- EXPLAINABLE AGENT OUTPUT ---")
    print(explanation)

    # Performance review / recognition
    print("\n Running Performance Recognition Agent...")
    recognition = run_performance_review_agent(task,users)
    print("\n--- PERFORMANCE REVIEW OUTPUT ---")
    print(recognition)

    # Conflict Resolution (NEW USE CASE)
    
    print("\nRunning Conflict Resolution Agent...")
    conflict_resolution = run_conflict_resolution_agent(task, teams, users)
    print("\n--- CONFLICT RESOLUTION OUTPUT ---")
    print(conflict_resolution)

    print("\nRunning Risk & Ethics Decision Agent...")
    risk_decision = run_risk_ethics_agent(task, data["teams"])
    print("\n--- RISK & ETHICS DECISION OUTPUT ---")
    print(risk_decision)

if __name__ == "__main__":
    main()
