import unittest

from skinner.utils import Transition


class TestUtils(unittest.TestCase):

    def test_transition(self):
        transition = Transition(state=1, action=2, next_state=3, reward=5)
        self.assertEqual(transition.state, 1)
        self.assertEqual(transition.action, 2)
        self.assertEqual(transition.next_state, 3)
        self.assertEqual(transition.reward, 5)
        self.assertEqual(len(transition), 4)
