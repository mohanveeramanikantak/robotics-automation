# Object Detection System Simulation

import random
import time

# Possible detected objects
objects = ["Person", "Car", "Bottle", "Box", "Chair"]

print("📷 Object Detection System Started")

time.sleep(1)

# Random object detection
detected_object = random.choice(objects)
confidence = random.randint(70, 99)

# Display result
print("Detected Object:", detected_object)
print("Confidence Level:", str(confidence) + "%")

time.sleep(1)

# AI decision logic
if detected_object == "Person":
    print("👤 Human Detected")

elif detected_object == "Car":
    print("🚗 Vehicle Detected")

else:
    print("📦 General Object Detected")

print("✅ Detection Process Completed")
