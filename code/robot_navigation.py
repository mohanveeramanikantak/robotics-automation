# Robot Navigation Simulation

import random

directions = ["FORWARD", "LEFT", "RIGHT", "BACKWARD"]

robot_move = random.choice(directions)

print("Robot Moving:", robot_move)

if robot_move == "FORWARD":
    print("✅ Path Clear")

elif robot_move == "LEFT":
    print("⬅️ Turning Left")

elif robot_move == "RIGHT":
    print("➡️ Turning Right")

else:
    print("🔄 Moving Backward")
