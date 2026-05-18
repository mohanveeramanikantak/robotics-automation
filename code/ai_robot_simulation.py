# AI Robot Simulation

import random
import time

# Possible robot actions
actions = [
    "Moving Forward",
    "Turning Left",
    "Turning Right",
    "Picking Object",
    "Stopping"
]

print("🤖 AI Robot Started")

time.sleep(1)

# Simulate robot decisions
for step in range(5):
    action = random.choice(actions)
    print(f"Step {step + 1}: {action}")
    time.sleep(1)

print("✅ Robot Task Completed")
