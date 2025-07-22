import pandas as pd
import matplotlib.pyplot as plt

# Load simulation data
df = pd.read_csv("../cpp_simulation/traffic_data.csv")

# Create a new figure
plt.figure(figsize=(12, 6))
ax = plt.gca()

# 1. Draw light background color bands (red or green)
time_points = df['Time'].unique()
for t in time_points:
    light_state = df[df['Time'] == t]['TrafficLight'].iloc[0]
    color = 'green' if light_state == 'GREEN' else 'red'
    ax.axvspan(t, t + 1, facecolor=color, alpha=0.1)

# 2. Plot vehicle positions
for vehicle_id in df['VehicleID'].unique():
    vehicle_data = df[df['VehicleID'] == vehicle_id]
    plt.plot(vehicle_data['Time'], vehicle_data['Position'], label=f'Vehicle {vehicle_id}')

# 3. Add labels and legend
plt.title("Vehicle Positions with Traffic Light Status")
plt.xlabel("Time (s)")
plt.ylabel("Position on Road")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

