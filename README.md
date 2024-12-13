# 2048 Game with Deep Q-Network (DQN)

## Project Overview | 项目概述

This project explores the use of Deep Q-Networks (DQN) to train an agent to play the game 2048. Through multiple iterations, the model evolves from a basic linear architecture to a Nature DQN with advanced features such as fixed target networks, experience replay, and batch training. Each version tackles specific challenges, improving the model's ability to learn strategies and achieve higher scores.

本项目探索了利用深度 Q 网络（DQN）训练智能体完成 2048 游戏的任务。通过多次迭代，模型从基础的线性结构逐步演化为具有固定目标网络、经验回放和批量训练等高级特性的 Nature DQN。每个版本针对特定问题进行优化，逐步提高模型学习策略和取得高分的能力。

---

## Version History | 版本记录

### Version 1 | 第 1 版
- **Description**: Implemented the basic 2048 game logic and optimized tile generation to make the game progress more smoothly (e.g., generating more "4" tiles at higher scores).
- **Features**:
  - Fully functional 2048 game logic.
  - Adjusted tile generation probabilities.
  
- **描述**：实现了基础的 2048 游戏逻辑，并优化了方块生成规则，使得游戏进展更加顺畅（例如在高分时生成更多 "4" 方块）。
- **功能**：
  - 完整的 2048 游戏逻辑。
  - 调整了方块生成的概率。

---

### Version 2 | 第 2 版
- **Description**: Introduced a basic DQN model with a fully connected network. However, the learning rate was unstable, and the model failed to converge after training for 10,000 epochs.
- **Features**:
  - Implemented a basic DQN with a fully connected architecture.
  - Observed unstable learning and poor performance.

- **描述**：引入了一个基于全连接网络的基础 DQN 模型。然而学习率不稳定，训练 10,000 轮后模型未能收敛。
- **功能**：
  - 实现了基础的全连接架构 DQN。
  - 发现学习不稳定且表现较差。

---

### Version 3 | 第 3 版
- **Description**: Added a punishment mechanism to penalize invalid moves and integrated experience replay with a NumPy-based implementation for faster batch sampling. The model showed signs of improvement, achieving scores around 300 but still struggled to converge efficiently.
- **Features**:
  - Introduced punishment rewards for stagnant states.
  - Rewrote experience replay with NumPy, enabling batch sampling.
  - Achieved moderate performance improvement (~300 points).

- **描述**：加入了惩罚机制以惩罚无效动作，并采用基于 NumPy 的经验回放机制实现更快的批量采样。模型性能有所改善，得分约为 300，但收敛效率仍较低。
- **功能**：
  - 引入了对停滞状态的惩罚奖励。
  - 用 NumPy 重写了经验回放机制，实现批量采样。
  - 模型性能有中度提升（约 300 分）。

---

### Version 4 | 第 4 版
- **Description**: Fixed bugs in batch sampling, added a fixed target network, and tuned hyperparameters. These improvements significantly enhanced training stability and convergence, with the model achieving scores of up to 744 after 30,000 epochs.
- **Features**:
  - Fixed bugs in the replay buffer implementation.
  - Added a fixed target network for stable Q-value updates.
  - Enabled batch training for faster and smoother learning.
  - Tuned key hyperparameters (e.g., learning rate, discount factor).

- **描述**：修复了批量采样中的错误，加入了固定目标网络并调整了超参数。这些改进显著提高了训练稳定性和收敛效果，模型在训练 30,000 轮后得分达到 744。
- **功能**：
  - 修复了经验回放实现中的错误。
  - 添加了固定目标网络以稳定 Q 值更新。
  - 引入批量训练，加快了训练速度并平滑了学习过程。
  - 调整了关键超参数（如学习率、折扣因子）。

---

## Future Work | 未来工作

1. Experiment with prioritized experience replay to further optimize sample efficiency.  
2. Explore alternative architectures, such as Double DQN or Dueling DQN.  
3. Investigate strategies to increase the model’s ability to achieve higher scores.

1. 尝试使用优先级经验回放机制进一步优化样本利用率。  
2. 探索替代架构，如 Double DQN 或 Dueling DQN。  
3. 研究增强模型得分能力的策略。

---

## How to Run | 如何运行

### Using Google Colab (Recommended)
1. Open the project in Google Colab:
   - Upload the `.ipynb` file to your Google Drive.
   - Open the Notebook in Google Colab by right-clicking the file and selecting **"Open with" > "Google Colab"**.
2. Enable GPU:
   - Go to **Runtime** > **Change runtime type**.
   - Select **GPU** under "Hardware accelerator."
3. Run all cells:
   - Click **Runtime** > **Run all** to execute the Notebook.

### Using jupyter notebook

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/2048-dqn.git
   cd 2048-dqn
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
I strongly recommend installing PyTorch from their [official website](https://pytorch.org/) to avoid potential issues during installation.  
如果您想要在本地运行代码，我强烈建议您通过 PyTorch 的 [官网](https://pytorch.org/) 安装 PyTorch，以避免安装过程中遇到的潜在问题。

4. Open the .ipynb file using Jupyter Notebook:
   ```bash
      jupyter notebook NatureDQN2048_v4.ipynb
   ```
5. Run all cells sequentially

---
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

