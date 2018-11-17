import gym


if __name__ == '__main__':

    env = gym.make('CartPole-v0')

    env.render()

    env.close()
