import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 读取CSV文件
file_path = 'paperwork/data/bridgedisp/datatest100steps600second_nodutyratio.csv'
df = pd.read_csv(file_path)

# 打印数据基本信息
print("数据基本信息：")
print(df.info())
print("\n数据前5行：")
print(df.head())

# 创建图形
plt.figure(figsize=(15, 10))

# 绘制时间序列图
plt.subplot(2, 1, 1)
plt.plot(df.index, df.iloc[:, 0], label='位移数据')
plt.title('桥梁位移时间序列')
plt.xlabel('时间步')
plt.ylabel('位移')
plt.legend()
plt.grid(True)

# 绘制直方图
plt.subplot(2, 1, 2)
plt.hist(df.iloc[:, 0], bins=50, density=True, alpha=0.7)
plt.title('位移分布直方图')
plt.xlabel('位移值')
plt.ylabel('频率')
plt.grid(True)

# 调整布局
plt.tight_layout()

# 保存图片
plt.savefig('displacement_analysis.png', dpi=300, bbox_inches='tight')

# 显示图形
plt.show()

# 计算基本统计量
print("\n基本统计量：")
print(df.describe()) 