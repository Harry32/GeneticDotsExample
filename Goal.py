import pygame


class Goal:

    def __init__(self, position):

        self.position = position

    def show(self, background):
        pygame.draw.circle(background, (0, 0, 0), self.position, 7)
        pygame.draw.circle(background, (255, 0, 0), self.position, 5)

    def getPosition(self):
        return self.position
