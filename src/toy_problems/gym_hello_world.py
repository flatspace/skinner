import gym
import torch
from baselines.common.atari_wrappers import wrap_deepmind

import torch.nn as nn


class Policy(nn.Module):

    def __init__(self):
        super(Policy, self).__init__()

        self.conv = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=5, stride=2),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.Conv2d(16, 32, kernel_size=5, stride=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.Conv2d(32, 32, kernel_size=5, stride=2),
            nn.BatchNorm2d(32),
            nn.ReLU())

        self.fc = nn.Linear(448, 2)

        def forward(self, x: torch.Tensor):
            x = self.conv(x)
            return self.fc(x.view(x.size(0), -1))


if __name__ == '__main__':
    env = gym.make('CartPole-v1')
    env.reset()
    for t in range(1000):
        env.render()
        observation, reward, done, info = env.step(env.action_space.sample())  # take a random action
        if done:
            print("Episode finished after {} timesteps".format(t + 1))
            env.reset()
    env.close()
