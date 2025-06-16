import matplotlib
matplotlib.use('TkAgg')  # 或者 'Qt5Agg'
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from matplotlib import ticker

# 设置全局字体为新罗马
config = {
    "font.family": 'Times New Roman',
    "font.size": 18,
    "mathtext.fontset": 'stix'
}
# 更新字体配置
plt.rcParams.update(config)

def read_second_column(input_file):
    # 用于存储第二列的数据
    second_column_data = []
    with open(input_file, 'r', encoding='utf-8') as infile:
        # 跳过第一行
        next(infile)
        for line in infile:
            # 去掉行末的换行符，并分割成两列
            columns = line.strip().split('\t')
            if len(columns) > 1:
                # 读取第二列数据
                second_column_data.append(float(columns[1]))
    # 将列表转换为 NumPy 数组
    return np.array(second_column_data)

# 设置文件路径
csv_path = r'D:\Research\Papers\1_paperwork\PHD_4thPaper_FundMultiFanWindVIV\PlotCode\2-非定常风场下桥梁振动位移\给流行的云\线性上升下降\result\线性信号上升无翼板扰动\Displacement.csv'  # 请替换为实际路径
txt_path = r'D:\Research\Papers\1_paperwork\PHD_4thPaper_FundMultiFanWindVIV\PlotCode\2-非定常风场下桥梁振动位移\给流行的云\线性上升下降\result\线性信号上升无翼板扰动\windspeed.txt'    # 请替换为实际路径

# 读取数据
df = pd.read_csv(csv_path, low_memory=False)

# 创建图形
fig, axs = plt.subplots(2, 1, figsize=(7, 5), tight_layout=True)

# 1. 风速图
x_0 = np.linspace(0, 300, 300000)
y_0 = read_second_column(txt_path)

# 从数组中采样每100个点里面的一个点
sampled_indices = np.arange(0, 300000, 100)
x_0 = x_0[sampled_indices]
y_0 = y_0[sampled_indices]

# 计算平均值
average_points = 15  # 每n个点取平均
average_u1 = np.array([y_0[i:i+average_points].mean() 
                      for i in range(0, len(y_0), average_points)])
average_t = np.linspace(0, 300, len(average_u1))

# 绘制风速图
axs[0].plot(x_0, y_0, lw=1, alpha=0.5)
axs[0].plot(average_t, average_u1, c='green', lw=1.6)

# 设置风速图格式
axs[0].xaxis.set_minor_locator(ticker.MultipleLocator(25))
axs[0].yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
axs[0].set_ylim(0, 4.1)
axs[0].set_yticks(np.arange(0, 5, 1))
axs[0].yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
axs[0].set_ylabel('Wind velocity \n(m/s)\n')

# 设置刻度样式
axs[0].tick_params(length=8, width=1)
axs[0].tick_params(which='minor', length=4, width=1)
axs[0].tick_params(direction='in')
axs[0].tick_params(which='minor', direction='in')

# 2. 位移图
x_1 = df['Time'][2:150002].astype(float).values
y_1 = df['Laser1234Ave'][2:150002].astype(float).values
sampled_indices = np.arange(0, 150000, 100)
x_1 = x_1[sampled_indices]
y_1 = y_1[sampled_indices]

# 读取RMS & Std
rms_1 = df['Laser1234Ave'][0]
std_1 = df['Laser1234Ave'][1]

# 绘制位移图
axs[1].plot(x_1, y_1, lw=1)

# 设置位移图格式
axs[1].xaxis.set_minor_locator(ticker.MultipleLocator(25))
axs[1].yaxis.set_minor_locator(ticker.MultipleLocator(1.25))
axs[1].set_ylim(-5.1, 5.1)
axs[1].set_yticks(np.arange(-5, 5.1, 2.5))
axs[1].set_ylabel('Displacement \n(cm)')
axs[1].set_xlabel('Time (s)')

# 设置刻度样式
axs[1].tick_params(length=8, width=1)
axs[1].tick_params(which='minor', length=4, width=1)
axs[1].tick_params(direction='in')
axs[1].tick_params(which='minor', direction='in')

# 添加RMS值
axs[1].text(0.99, 0.90, f'RMS = {rms_1:.3f}', fontsize=22,
            ha='right', va='top', transform=axs[1].transAxes)

# 保存图片
plt.savefig('output.png', dpi=600)
plt.savefig('output.svg')

# 显示图形
plt.show() 