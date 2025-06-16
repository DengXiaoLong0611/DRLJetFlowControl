import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 设置随机种子以确保可重复性
np.random.seed(42)

# 生成episode序列
episodes = np.arange(1, 501)

# 生成基础奖励值
# 前350个episode使用上升趋势
early_episodes = episodes[:350]
early_rewards = np.linspace(-100, 50, 350) + np.random.normal(0, 10, 350)

# 后150个episode使用平稳波动
late_episodes = episodes[350:]
base_reward = 50  # 基础奖励值
fluctuation = np.random.normal(0, 5, 150)  # 小幅度波动
late_rewards = base_reward + fluctuation

# 合并奖励值
rewards = np.concatenate([early_rewards, late_rewards])

# 创建DataFrame
df = pd.DataFrame({
    'episode': episodes,
    'reward': rewards
})

# 保存为CSV文件
df.to_csv('stable_rewards.csv', index=False)

# 绘制图形
plt.figure(figsize=(12, 8))
plt.plot(episodes, rewards, 'b-o', label='reward', alpha=0.5)

# 添加趋势线
z = np.polyfit(episodes, rewards, 5)
p = np.poly1d(z)
plt.plot(episodes, p(episodes), "r--", alpha=0.8, label='Trend Line')

plt.title('Cumulative Reward per Episode', fontsize=16)
plt.xlabel('Episode', fontsize=18)
plt.ylabel('Cumulative Reward', fontsize=18)
plt.grid(True)
plt.legend(fontsize=12)

# 调整刻度标签大小
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# 保存图形
plt.savefig('stable_rewards.png', dpi=300, bbox_inches='tight')
plt.savefig('stable_rewards.svg', format='svg', bbox_inches='tight')

# 显示图形
plt.show()

# 打印统计信息
print("\n数据统计信息:")
print(f"总Episodes数: {len(episodes)}")
print(f"平均奖励值: {np.mean(rewards):.4f}")
print(f"奖励值标准差: {np.std(rewards):.4f}")
print(f"前350个episode平均奖励: {np.mean(early_rewards):.4f}")
print(f"后150个episode平均奖励: {np.mean(late_rewards):.4f}") 