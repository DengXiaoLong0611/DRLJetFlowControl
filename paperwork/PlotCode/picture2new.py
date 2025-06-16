import re
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker

# 设置全局字体为新罗马
config = {
    "font.family": 'Times New Roman',
    "font.size": 18,
    "mathtext.fontset": 'stix'
}
plt.rcParams.update(config)

# 读取数据
log_file = r'D:\Research\PHDProject\Code\Code_running\大风洞的合成射流DRL训练\Year2025\2-dutyratio20250525\run\save\1\DRLlog.txt'
steps, voltages, displacements = [], [], []

with open(log_file, 'r') as file:
    lines = file.readlines()
    last_50_lines = lines[-50:]
    for i, line in enumerate(last_50_lines):
        voltage_match = re.search(r'voltage: ([-]?\d+\.\d+)', line)
        displacement_match = re.search(r'VIVRMS: ([-]?\d+\.\d+)', line)
        if all([voltage_match, displacement_match]):
            step = i + 1
            voltage = float(voltage_match.group(1))
            displacement = float(displacement_match.group(1))
            steps.append(step)
            voltages.append(voltage)
            displacements.append(displacement)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 5), tight_layout=True)

# 电压
ax1.plot(steps, voltages, 'b-', lw=1, label='Voltage')
ax1.set_xlabel('Step', fontsize=18)
ax1.set_ylabel('Voltage (V)', fontsize=18)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(fontsize=18)
ax1.tick_params(axis='both', which='major', labelsize=18)
ax1.set_xticks(range(5, 55, 5))
ax1.set_xlim(0, 52)
ax1.tick_params(length=8, width=1)
ax1.tick_params(which='minor', length=4, width=1)
ax1.tick_params(direction='in')
ax1.tick_params(which='minor', direction='in')

# 位移
ax2.plot(steps, displacements, 'r-', lw=1, label='Displacement RMS')
ax2.set_xlabel('Step', fontsize=18)
ax2.set_ylabel('Displacement RMS (m)', fontsize=18)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend(fontsize=18)
ax2.tick_params(axis='both', which='major', labelsize=18)
ax2.set_xticks(range(5, 55, 5))
ax2.set_xlim(0, 52)
ax2.tick_params(length=8, width=1)
ax2.tick_params(which='minor', length=4, width=1)
ax2.tick_params(direction='in')
ax2.tick_params(which='minor', direction='in')
rms_value = np.sqrt(np.mean(np.array(displacements)**2))
ax2.text(0.99, 0.90, f'RMS = {rms_value:.3f}', fontsize=22,
         ha='right', va='top', transform=ax2.transAxes)

plt.tight_layout()
plt.savefig('last_episode_analysis.png', dpi=600, bbox_inches='tight')
plt.savefig('last_episode_analysis.svg', format='svg', bbox_inches='tight')
plt.show()

print("\nLast Episode Statistics:")
print(f"Average Voltage: {np.mean(voltages):.4f} V")
print(f"Voltage Std Dev: {np.std(voltages):.4f} V")
print(f"Average Displacement RMS: {np.mean(displacements):.4f} m")
print(f"Displacement RMS Std Dev: {np.std(displacements):.4f} m")