import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Load CSV
df = pd.read_csv("../cpp_simulation/traffic_data.csv")

vehicles = df['VehicleID'].unique()
time_steps = sorted(df['Time'].unique())

# Setup figure
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, max(time_steps))   # ensure consistent x-axis
ax.set_ylim(0, 110)               # ensure consistent y-axis
ax.set_title("Animated Traffic Simulation")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Position on Road")
ax.grid(True)

# Line objects for each vehicle (initialized empty)
lines = {}
for idx, vid in enumerate(vehicles):
    line, = ax.plot([], [], label=f'Vehicle {vid}', linewidth=2)
    lines[vid] = line

# Traffic light background
light_patch = ax.axvspan(0, 1, facecolor='red', alpha=0.1)
ax.legend()

# Update function
def update(frame):
    current_time = time_steps[frame]
    ax.set_title(f"Time: {current_time}s")

    # Update traffic light patch
    light_state = df[df['Time'] == current_time]['TrafficLight'].iloc[0]
    light_patch.set_xy([[0, 0], [current_time + 1, 0], [current_time + 1, 110], [0, 110], [0, 0]])
    light_patch.set_facecolor('green' if light_state == 'GREEN' else 'red')

    # Update vehicle lines
    for vid in vehicles:
        vdf = df[(df['VehicleID'] == vid) & (df['Time'] <= current_time)]
        x = vdf['Time'].values
        y = vdf['Position'].values
        lines[vid].set_data(x, y)

    return list(lines.values()) + [light_patch]

# Create and retain reference to animation
ani = animation.FuncAnimation(
    fig, update,
    frames=len(time_steps),
    interval=500,
    blit=False,  # <-- changed from True to False
    repeat=False
)

plt.tight_layout()
plt.show()
ani.save("traffic_simulation.gif", writer='pillow')

