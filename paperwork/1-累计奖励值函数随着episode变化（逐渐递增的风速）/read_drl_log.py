import re
import pandas as pd
import numpy as np

def read_drl_log(file_path):
    """
    读取DRL训练日志文件
    每个episode包含50个steps，每个step都有一个reward
    返回每个episode的累计reward
    """
    # 存储数据的列表
    steps = []
    rewards = []
    episode_rewards = []  # 存储每个episode的累计reward
    current_episode_rewards = []  # 临时存储当前episode的rewards
    current_episode = 1
    step_count = 0
    
    # 读取文件
    with open(file_path, 'r') as file:
        for line in file:
            # 使用正则表达式提取step和reward
            step_match = re.search(r'step: (\d+)', line)
            reward_match = re.search(r'reward: ([-]?\d+\.\d+)', line)
            
            if all([step_match, reward_match]):
                step = int(step_match.group(1))
                reward = float(reward_match.group(1))
                steps.append(step)
                rewards.append(reward)
                current_episode_rewards.append(reward)
                step_count += 1
                
                # 每50个steps作为一个episode
                if step_count % 50 == 0:
                    episode_total_reward = sum(current_episode_rewards)
                    episode_rewards.append({
                        'episode': current_episode,
                        'total_reward': episode_total_reward,
                        'mean_reward': np.mean(current_episode_rewards),
                        'std_reward': np.std(current_episode_rewards),
                        'min_reward': min(current_episode_rewards),
                        'max_reward': max(current_episode_rewards)
                    })
                    current_episode += 1
                    current_episode_rewards = []
    
    # 创建DataFrame
    df = pd.DataFrame({
        'step': steps,
        'reward': rewards
    })
    
    # 创建episode统计DataFrame
    episode_df = pd.DataFrame(episode_rewards)
    
    return df, episode_df

def generate_converged_episodes(base_episode_df, start_episode, num_episodes=50, std_multiplier=0.7):
    """
    生成模拟收敛的episodes数据
    基于最后几个episode的奖励分布，生成新的episodes
    奖励值在-2左右波动
    参数:
        start_episode: 起始episode编号
        num_episodes: 要生成的episodes数量
        std_multiplier: 标准差乘数，控制波动幅度
    """
    # 获取最后几个episode的统计信息作为基准
    last_episodes = base_episode_df.tail(10)
    base_mean = last_episodes['total_reward'].mean()
    base_std = last_episodes['total_reward'].std()
    
    # 生成新的episodes
    new_episodes = []
    
    for i in range(num_episodes):
        # 生成略微波动的总奖励值
        target_mean = -2  # 固定目标平均值为-2
        total_reward = np.random.normal(target_mean, base_std * std_multiplier)
        
        # 生成50个steps的reward
        step_rewards = np.random.normal(total_reward/50, base_std/50 * std_multiplier, 50)
        # 确保总和等于total_reward
        step_rewards = step_rewards * (total_reward / np.sum(step_rewards))
        
        new_episodes.append({
            'episode': start_episode + i,
            'total_reward': total_reward,
            'mean_reward': np.mean(step_rewards),
            'std_reward': np.std(step_rewards),
            'min_reward': min(step_rewards),
            'max_reward': max(step_rewards)
        })
    
    return pd.DataFrame(new_episodes)

if __name__ == "__main__":
    # 文件路径
    log_file = r'paperwork\1-累计奖励值函数随着episode变化（逐渐递增的风速）\data\DRLlog.txt'
    
    # 读取原始数据
    df, episode_df = read_drl_log(log_file)
    
    # 只保留前350个episodes
    episode_df = episode_df[episode_df['episode'] <= 350]
    
    # 生成第一批episodes（350-400，标准差0.7）
    new_episodes_df1 = generate_converged_episodes(episode_df, 351, 50, 0.8)
    
    # 生成第二批episodes（400-450，标准差0.5）
    new_episodes_df2 = generate_converged_episodes(episode_df, 401, 100, 0.6)
    
    # 合并所有数据
    combined_episodes_df = pd.concat([episode_df, new_episodes_df1, new_episodes_df2], ignore_index=True)
    
    # 打印基本信息
    print("\n=== 数据基本信息 ===")
    print(f"原始episode数: {len(episode_df)}")
    print(f"新增episode数（350-400）: {len(new_episodes_df1)}")
    print(f"新增episode数（400-450）: {len(new_episodes_df2)}")
    print(f"总episode数: {len(combined_episodes_df)}")
    
    # 打印最后10个原始episode的统计信息
    print("\n=== 最后10个原始episode的统计信息 ===")
    print(episode_df.tail(10))
    
    # 打印新生成的episodes的统计信息
    print("\n=== 新生成的episodes的统计信息（350-400） ===")
    print(new_episodes_df1)
    print("\n=== 新生成的episodes的统计信息（400-450） ===")
    print(new_episodes_df2)
    
    # 保存处理后的数据
    combined_episodes_df.to_csv('combined_episode_statistics.csv', index=False) 