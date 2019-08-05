import pygame


class Obstacle:

    def __init__(self, color, rectangle):

        self.color = color
        self.rectangle = rectangle

    def show(self, surface):
        pygame.draw.rect(surface, self.color, self.rectangle)

    def checkColision(self, dotX, dotY):

        if dotX >= self.rectangle[0] and dotX <= (self.rectangle[0] + self.rectangle[2]) and dotY >= self.rectangle[1] and dotY <= (self.rectangle[1] + self.rectangle[3]):
            return True
        else:
            return False
