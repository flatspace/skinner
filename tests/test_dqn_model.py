import unittest

from skinner.dqn_model import DQN


class TestDQN(unittest.TestCase):

    def test_init(self):
        net = DQN([4, 84, 84], 4)
        z= net.modules()[0]
        x=1

if __name__ == '__main__':
    unittest.main()