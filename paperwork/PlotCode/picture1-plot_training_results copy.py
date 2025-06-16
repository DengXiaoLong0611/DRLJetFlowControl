import re
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

# Set font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'

# Read data from CSV
df = pd.read_csv(r'D:\Research\PHDProject\Code\Code_running\大风洞的合成射流DRL训练\Year2025\2-dutyratio20250525\test\save\1\traj.csv')  # 修改为相对路径
episodes = df['episode'].values
episode_rewards = df['reward'].values

# Remove outliers
episode_rewards_array = np.array(episode_rewards)
z_scores = np.abs(stats.zscore(episode_rewards_array))
outliers = (z_scores > 3)  # Use 3 standard deviations as threshold
filtered_episodes = np.array(episodes)[~outliers]
filtered_rewards = episode_rewards_array[~outliers]

# Create plot
plt.style.use('seaborn')
plt.figure(figsize=(12, 8))

# Plot filtered data (blue line)
plt.plot(filtered_episodes, filtered_rewards, 'b-o', label='reward')

# Add trend line (polynomial fit)
z = np.polyfit(filtered_episodes, filtered_rewards, 5)  # 使用5次多项式拟合
p = np.poly1d(z)
plt.plot(filtered_episodes, p(filtered_episodes), "r--", alpha=0.8, label='Trend Line')

plt.title('Cumulative Reward per Episode (50 steps per Episode)', fontsize=16)
plt.xlabel('Episode', fontsize=18)
plt.ylabel('Cumulative Reward', fontsize=18)
plt.grid(True)
plt.legend(fontsize=12)

# Adjust tick label sizes
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Save plots
plt.savefig('../../reward_vs_episodes.png', dpi=300, bbox_inches='tight')
plt.savefig('../../reward_vs_episodes.svg', format='svg', bbox_inches='tight')

# Display plot
plt.show()

# Print statistics
print("\nTraining Statistics:")
print(f"Total Episodes: {len(episodes)}")
print(f"Number of Outliers: {np.sum(outliers)}")
print(f"Average Cumulative Reward: {np.mean(filtered_rewards):.4f}")
print(f"Cumulative Reward Std Dev: {np.std(filtered_rewards):.4f}")
print(f"Trend Line Coefficients: {z}")  # 打印多项式系数 