import sys
import pygame
from Population import Population
from Goal import Goal
from Obstacle import Obstacle


class PgWindow(object):

    def __init__(self, width=800, height=800):

        self.running = False
        self.fps = 30
        self.width = width
        self.height = height
        self.playtime = 0

        # Initialize pygame module
        pygame.init()

        self.clock = pygame.time.Clock()
        # Set screen size of pygame window
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Create an empty surface
        # Convert the surface to make blitting faster
        self.background = pygame.Surface(self.screen.get_size()).convert()
        # Fill the background with white
        self.background.fill((255, 255, 255))

        self.font = pygame.font.SysFont("calibri", 20)

        self.population = None
        self.goal = None
        self.obstacles = []

        self.setElements()

        # Blitting is the equivalent to paint the screen
        # Without blintting the background isn't visible
        self.screen.blit(self.background, (0, 0))

    def setElements(self):

        self.goal = Goal((int(self.width / 2), int(self.height * 0.05)))
        self.goal.show(self.background)

        # self.obstacles.append(Obstacle((0, 0, 255), (100, 300, 600, 30)))
        #
        # self.obstacles[0].show(self.background)

        self.population = Population((int(self.width / 2), int(self.height*0.95)), 1000, self.goal.getPosition())

    def onEvent(self, event):

        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False

    def onLoop(self):
        pass

    def onRender(self):
        # self.goal.show(self.background)
        textTime = self.font.render("Time: {:.2f} seconds.".format(self.playtime), True, (0, 0, 0))
        textGeneration = self.font.render("Generation: {:d}".format(self.population.generation), True, (0, 0, 0))

        self.screen.blit(self.background, (0, 0))
        self.screen.blit(textTime, (25, 25))
        self.screen.blit(textGeneration, (700, 25))

        if self.population.allDead():
            # Genetic algorithm
            self.population.calculateFitness()
            self.population.nauralSelection()
            self.population.mutateDemBabies()
        else:
            self.population.move(self.obstacles)
            self.population.show(self.screen)

        pygame.display.flip()

    def run(self):

        self.running = True

        while self.running:
            milliseconds = self.playtime + self.clock.tick(self.fps)
            self.playtime = self.playtime + milliseconds / 1000
            for event in pygame.event.get():
                self.onEvent(event)

            self.onLoop()
            self.onRender()

        pygame.quit()
        sys.exit()
