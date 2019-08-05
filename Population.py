from operator import attrgetter
from numpy.random import uniform, choice
from Dot import Dot


class Population:

    def __init__(self, position, size, goalPosition):

        self.dots = []

        for i in range(size):
            self.dots.append(Dot(position, goalPosition))
            i += 1

        self.initialPosition = position
        self.goalPosition = goalPosition
        self.size = size
        self.fitnessSum = 0
        self.generation = 1
        self.minSteps = 400
        self.bestDot = None

    def show(self, container):

        for dot in self.dots:
            dot.show(container)

    def move(self, obstacles=[]):

        for dot in self.dots:
            if not dot.dead and dot.brain.step > self.minSteps:
                dot.dead = True

            dot.move(obstacles)

    def calculateFitness(self):

        for dot in self.dots:
            dot.calculateFitness()

    def allDead(self):

        for dot in self.dots:
            if not dot.dead and not dot.reachedGoal:
                return False

        return True

    def nauralSelection(self):

        newDots = []
        self.setBestDot()
        self.__calculateFitnessSum()

        for i in range(self.size):

            parentDot = self.__selectParent()
            baby = parentDot.gimmeBaby(self.initialPosition)

            newDots.append(baby)

            i += 1

        newDots.append(self.bestDot)

        self.dots = newDots
        self.generation = self.generation + 1

    def mutateDemBabies(self):

        for dot in self.dots:
            dot.brain.mutate()

    def setBestDot(self):
        self.bestDot = max(self.dots, key=attrgetter('fitness'))

        if self.bestDot.reachedGoal:
            self.minSteps = self.bestDot.brain.step

        self.bestDot.brain.step = 0
        self.bestDot.dead = False
        self.bestDot.reachedGoal = False
        self.bestDot.velocity = (0, 0)
        self.bestDot.fitness = 0
        self.bestDot.position = self.initialPosition
        self.bestDot.setColor((0, 255, 0))

    def __calculateFitnessSum(self):

        for dot in self.dots:
            self.fitnessSum = self.fitnessSum + dot.getFitness()

    def __selectParent(self):

        rand = uniform(0, self.fitnessSum)
        runningSum = 0

        for dot in self.dots:
            runningSum = runningSum + dot.fitness

            if runningSum >= rand:
                return dot

        return choice(self.dots)
