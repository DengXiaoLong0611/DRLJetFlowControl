import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# 设置中文字体和Times New Roman
plt.rcParams['font.family'] = ['SimHei', 'Times New Roman']
plt.rcParams['mathtext.fontset'] = 'stix'

# 读取数据
df = pd.read_csv(r'paperwork\1-累计奖励值函数随着episode变化（逐渐递增的风速）\data\combined_episode_statistics.csv')

# 只保留前350个episode的数据
df = df[df['episode'] <= 550]

# 创建图形
plt.figure(figsize=(15, 10))

# 创建单个子图
fig, ax = plt.subplots(figsize=(15, 8))
fig.suptitle('DRL训练过程分析', fontsize=24)

# 绘制累计奖励随episode的变化
ax.plot(df['episode'], df['total_reward'], 'b-', label='累计奖励', alpha=0.6, linewidth=2)
ax.set_title('每个Episode的累计奖励变化', fontsize=20)
ax.set_xlabel('Episode', fontsize=18)
ax.set_ylabel('累计奖励', fontsize=18)
ax.grid(True, linestyle='--', alpha=0.7)

# 添加趋势线（10次多项式拟合）
z = np.polyfit(df['episode'], df['total_reward'], 10)
p = np.poly1d(z)
ax.plot(df['episode'], p(df['episode']), "r--", label='趋势线', alpha=0.8, linewidth=2)

# 添加移动平均线
window_size = 10
moving_avg = df['total_reward'].rolling(window=window_size).mean()
ax.plot(df['episode'], moving_avg, 'g-', label=f'{window_size}个Episode移动平均', alpha=0.8, linewidth=2)

# 设置刻度字体大小
ax.tick_params(axis='both', which='major', labelsize=16)

# 设置图例字体大小
ax.legend(fontsize=16)

# 调整布局
plt.tight_layout()

# 保存图片
plt.savefig(r'paperwork\1-累计奖励值函数随着episode变化（逐渐递增的风速）\training_reward.png', dpi=600, bbox_inches='tight')
plt.savefig(r'paperwork\1-累计奖励值函数随着episode变化（逐渐递增的风速）\training_reward.svg', format='svg', bbox_inches='tight')

# 显示图形
plt.show()

# 打印统计信息
print("\n=== 训练统计信息 ===")
print(f"总Episode数: {len(df)}")
print(f"平均累计奖励: {df['total_reward'].mean():.4f}")
print(f"累计奖励标准差: {df['total_reward'].std():.4f}")
print(f"最大累计奖励: {df['total_reward'].max():.4f}")
print(f"最小累计奖励: {df['total_reward'].min():.4f}")

# 计算最后50个episodes的统计信息
last_50_episodes = df.tail(50)
print("\n=== 最后50个Episodes的统计信息 ===")
print(f"平均累计奖励: {last_50_episodes['total_reward'].mean():.4f}")
print(f"累计奖励标准差: {last_50_episodes['total_reward'].std():.4f}")
print(f"奖励变化率: {(last_50_episodes['total_reward'].std() / last_50_episodes['total_reward'].mean() * 100):.2f}%") 