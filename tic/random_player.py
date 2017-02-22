import random

class RandomPlayer(object):
    def select_action(self):
        return random.randint(0, 3), random.randint(0, 3)