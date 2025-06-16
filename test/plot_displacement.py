import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 读取CSV文件
file_path = r'D:\Research\PHDProject\Code\Code_running\大风洞的合成射流DRL训练\Year2025\2-dutyratio20250525\test\paperwork\data\bridgedisp\datatest100steps600second_nodutyratio.csv'
df = pd.read_csv(file_path, low_memory=False)

# 确保Time列是数值类型
df['Time'] = pd.to_numeric(df['Time'], errors='coerce')
df['Laser1234Ave'] = pd.to_numeric(df['Laser1234Ave'], errors='coerce')

# 删除任何包含NaN的行
df = df.dropna(subset=['Time', 'Laser1234Ave'])

# 打印列名，用于调试
print("CSV文件的列名：")
print(df.columns.tolist())

# 创建图形
plt.figure(figsize=(15, 8))

# 绘制时间序列图
plt.plot(df['Time'], df['Laser1234Ave'], label='位移数据', linewidth=1)
plt.title('桥梁位移时间序列', fontsize=14)
plt.xlabel('时间 (s)', fontsize=12)
plt.ylabel('位移 (mm)', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# 设置x轴刻度间隔
max_time = df['Time'].max()
plt.xticks(np.arange(0, max_time + 1, 60))  # 每60秒显示一个刻度

# 调整布局
plt.tight_layout()

# 保存图片
plt.savefig('bridge_displacement.png', dpi=300, bbox_inches='tight')

# 显示图形
plt.show()

# 打印基本统计信息
print("\n位移数据基本统计量：")
print(df['Laser1234Ave'].describe()) 