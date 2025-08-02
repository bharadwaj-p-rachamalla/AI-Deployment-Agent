# Entry point for the deployment agent
from chatgpt_bridge import handle_command

if __name__ == "__main__":
    print("AI Deployment Agent is active and awaiting instructions.")
    handle_command()

import time

print("AI Deployment Agent is now idle and waiting...")

# Keep the process alive
while True:
    time.sleep(60)
