import unittest
import random

from skinner.memories import FixedSizeMemory


class TestReplayMemory(unittest.TestCase):

    def test_sample_empty_memory_raises_value_error(self):
        empty_mem = FixedSizeMemory(5)
        with self.assertRaises(ValueError):
            empty_mem.sample(1)

    def test_sample_without_repetition(self):
        memory = filled_random_memory(5)
        for _ in range(40):
            self.assertEqual(set(memory.sample(5)), set(memory.sample(5)))

    def test_push_increases_memory_size_until_capacity(self):
        mem = FixedSizeMemory(5)
        for i in range(1,6):
            mem.push(i)
            self.assertEqual(len(mem), i)
        mem.push(6)
        self.assertEqual(len(mem), 5)

    def test_push_replaces_oldest_element_first(self):
        mem = FixedSizeMemory(5)
        for i in range(1, 6):
            mem.push(i)
            self.assertEqual(len(mem), i)
        mem.push(6)
        self.assertTrue(1 not in set(mem.sample(5)))


def filled_random_memory(size):
    mem = FixedSizeMemory(size)
    for _ in range(size):
        mem.push(random.random())
    return mem


if __name__ == '__main__':
    unittest.main()