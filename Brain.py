import math
from copy import deepcopy
# from random import uniform, randint
from numpy.random import randint, uniform


class Brain:

    def __init__(self, size, clone=False):

        self.directions = []
        self.size = size
        self.step = 0

        if not clone:
            self.randomize()

    def randomize(self):

        # maxValue = 2 * math.pi
        # minValue = maxValue * (-1)
        # values = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]

        for i in range(self.size):
            # self.directions.append((int(uniform(minValue, maxValue)), int(uniform(minValue, maxValue))))
            self.directions.append((randint(-4, 6), randint(-5, 6)))
            # self.directions.append((choice(values), choice(values)))

    def getNextDirection(self):

        direction = None

        if self.step != self.size:
            direction = self.directions[self.step]
            self.step = self.step + 1

        return direction

    def clone(self):
        clone = Brain(400, True)
        clone.directions = self.directions
        return clone

    def mutate(self):

        mutationRate = 0.01

        for direction in self.directions:
            rand = uniform(0, 1)

            if rand < mutationRate:
                direction = (randint(-5, 6), randint(-5, 6))
