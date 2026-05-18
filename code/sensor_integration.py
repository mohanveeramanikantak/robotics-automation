# Sensor Integration Simulation

import random
import time

print("📡 Sensor System Activated")

time.sleep(1)

# Simulated sensor readings
temperature = random.randint(20, 40)
distance = random.randint(1, 100)
light = random.randint(0, 100)

# Display readings
print("🌡 Temperature:", temperature, "°C")
print("📏 Distance:", distance, "cm")
print("💡 Light Level:", light, "%")

time.sleep(1)

# Basic automation logic
if distance < 20:
    print("⚠️ Obstacle Detected")

if temperature > 35:
    print("🔥 High Temperature Warning")

if light < 30:
    print("🌙 Low Light Environment")
else:
    print("✅ Sensors Operating Normally")
