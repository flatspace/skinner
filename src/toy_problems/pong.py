import gym

from skinner import dqn_model
from toy_problems import atari_wrappers

env_name = 'PongNoFrameskip-v4'

if __name__ == "__main__":

    env = gym.make(env_name)
    env = atari_wrappers.wrap_dqn(env)
    input_shape = env.observation_space.shape
    n_actions = env.action_space.n
    net = dqn_model.create_net(env)
    x=1
