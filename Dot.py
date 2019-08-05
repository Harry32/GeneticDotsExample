import pygame
import math
from Brain import Brain


class Dot:

    def __init__(self, position, goalPosition, baby=False):

        self.brain = Brain(400, baby)

        self.dead = False
        self.reachedGoal = False
        self.fitness = 0
        self.goalPosition = goalPosition

        self.position = position
        self.velocity = (0, 0)
        self.acceleration = ()
        self.color = (0, 0, 0)

    def show(self, container):

        pygame.draw.circle(container, self.color, self.position, 3)

    def move(self, obstacles=[]):

        if not self.dead and not self.reachedGoal:
            self.acceleration = self.brain.getNextDirection()

            if self.acceleration is None:
                self.dead = True
            else:
                self.__updateVelocity()
                self.__updatePosition(obstacles)

    def calculateFitness(self):

        if self.reachedGoal:
            self.fitness = 1.0/16 + 1000/(self.brain.step**2)
        else:
            distance = math.hypot((self.position[0] - self.goalPosition[0]), (self.position[1] - self.goalPosition[1]))

            if distance == 0:
                distance = 1

            self.fitness = 1.0/(distance**2)

    def getFitness(self):
        return self.fitness

    def gimmeBaby(self, position):

        baby = Dot(position, self.goalPosition, True)
        baby.brain = self.brain.clone()

        return baby

    def setColor(self, color):
        self.color = color

    def __updateVelocity(self):

        vx = self.velocity[0] + self.acceleration[0]
        vy = self.velocity[1] + self.acceleration[1]

        if vx > 5:
            vx = 5

        if vy > 5:
            vy = 5

        self.velocity = (vx, vy)

    def __updatePosition(self, obstacles=[]):

        px = self.position[0] + self.velocity[0]
        py = self.position[1] + self.velocity[1]

        distance = math.hypot((px - self.goalPosition[0]), (py - self.goalPosition[1]))

        if distance < 6:
            self.reachedGoal = True
        else:

            for obstacle in obstacles:
                if obstacle.checkColision(px, py):
                    self.dead = True

            if px < 0:
                px = 0
                self.dead = True
            elif px > 800:
                px = 800
                self.dead = True

            if py < 0:
                py = 0
                self.dead = True
            elif py > 800:
                py = 800
                self.dead = True

        self.position = (px, py)
