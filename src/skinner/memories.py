import random


class FifoFixedSizeMemory(object):

    def __init__(self, capacity: int):
        """ A first in, first out queue with a fixed maximum capacity """
        self.capacity = capacity
        self.memory = []
        self.position = 0

    def commit(self, *args):
        """ Commit args to memory. """
        if len(self.memory) < self.capacity:
            self.memory.append(None)
        self.memory[self.position] = args
        self.position = (self.position + 1) % self.capacity

    def sample(self, batch_size: int):
        """ Randomly sample a number of elements from memory without replacement."""
        return random.sample(self.memory, batch_size)

    def __len__(self):
        return len(self.memory)
