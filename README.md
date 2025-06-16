# Synthetic Jet DRL Control System

基于深度强化学习的合成射流控制系统。

## 项目结构

```
.
├── run/                    # 主要代码目录
│   ├── Env/               # 强化学习环境定义
│   ├── tools/             # 工具函数
│   ├── deploy/            # 部署相关代码
│   └── main.py            # 主程序入口
├── test/                  # 测试代码
└── paperwork/             # 文档
```

## 主要功能

- 基于SAC算法的强化学习控制
- 支持电压和频率控制
- 包含瞬态和稳态控制
- 实时数据采集和处理

## 环境要求

- Python 3.8+
- PyTorch
- Stable-Baselines3
- Gym

## 使用方法

1. 训练模式：
```python
run = 'train'
```

2. 继续训练模式：
```python
run = 'train_load'
```

3. 评估模式：
```python
run = 'eval'
```

## 许可证

MIT License 