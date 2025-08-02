# Entry point for the deployment agent
from chatgpt_bridge import handle_command

if __name__ == "__main__":
    print("AI Deployment Agent is active and awaiting instructions.")
    handle_command()
