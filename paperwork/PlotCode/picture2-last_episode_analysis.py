import re
import matplotlib.pyplot as plt
import numpy as np

# Set font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'

# Read data
log_file = r'D:\Research\PHDProject\Code\Code_running\大风洞的合成射流DRL训练\Year2025\2-dutyratio20250525\run\save\1\DRLlog.txt'

# Initialize lists for the last episode
steps = []
voltages = []
displacements = []

# Read the last 50 steps from the log file
with open(log_file, 'r') as file:
    lines = file.readlines()
    last_50_lines = lines[-50:]  # Get the last 50 lines
    
    for i, line in enumerate(last_50_lines):
        # Extract data using regex
        voltage_match = re.search(r'voltage: ([-]?\d+\.\d+)', line)
        displacement_match = re.search(r'VIVRMS: ([-]?\d+\.\d+)', line)
        
        if all([voltage_match, displacement_match]):
            step = i + 1  # Use 1-50 as step numbers
            voltage = float(voltage_match.group(1))
            displacement = float(displacement_match.group(1))
            
            steps.append(step)
            voltages.append(voltage)
            displacements.append(displacement)

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
fig.suptitle('Train test (50 steps)', fontsize=16)

# Plot voltages (actions)
ax1.plot(steps, voltages, 'b-o', label='Voltage')
ax1.set_xlabel('Step', fontsize=14)
ax1.set_ylabel('Voltage (V)', fontsize=14)
ax1.grid(True)
ax1.legend(fontsize=12)
ax1.tick_params(axis='both', which='major', labelsize=12)
ax1.set_xticks(range(5, 55, 5))  # Set x-axis ticks every 5 steps from 5 to 50
ax1.set_xlim(0, 52)  # Set x-axis range from 1 to 50

# Plot displacements
ax2.plot(steps, displacements, 'r-o', label='Displacement RMS')
ax2.set_xlabel('Step', fontsize=14)
ax2.set_ylabel('Displacement RMS (m)', fontsize=14)
ax2.grid(True)
ax2.legend(fontsize=12)
ax2.tick_params(axis='both', which='major', labelsize=12)
ax2.set_xticks(range(5, 55, 5))  # Set x-axis ticks every 5 steps from 5 to 50
ax2.set_xlim(0, 52)  # Set x-axis range from 1 to 50

# Adjust layout
plt.tight_layout()

# Save plots
plt.savefig('last_episode_analysis.png', dpi=300, bbox_inches='tight')
plt.savefig('last_episode_analysis.svg', format='svg', bbox_inches='tight')

# Display plot
plt.show()

# Print statistics
print("\nLast Episode Statistics:")
print(f"Average Voltage: {np.mean(voltages):.4f} V")
print(f"Voltage Std Dev: {np.std(voltages):.4f} V")
print(f"Average Displacement RMS: {np.mean(displacements):.4f} m")
print(f"Displacement RMS Std Dev: {np.std(displacements):.4f} m")