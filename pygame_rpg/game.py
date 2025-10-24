import pygame

from .entity import *

from .settings import Settings

class Game:

    def __init__(self):

        # set up settings
        self.settings = Settings()
        scale = self.settings.data["scale"]

        pygame.init()
        game_size = width, height = 160, 120
        self.window_size = width, height = round(160 * scale), round(120 * scale) # this will be based on ur settings, gotta add an editor tho

        self.screen = pygame.Surface(game_size) # the game
        self.window = pygame.display.set_mode(self.window_size) # and scaled ggame

        pygame.display.set_caption("Nut Simulator: He Returns...")

        self.clock = pygame.time.Clock()

        

    def run(self):

        # TODO: make a list of entities like most games

        self.test = Entity(0, 0, "assets/img/nutstill.png")

        self.player = Player(0, 0, "assets/img/nutstill.png")
        
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # if it quits running is false
                    running = False

            self.update(event) # pass events into running which should be passed into objects n stuff

            self.clock.tick(30)

    def update(self, event):
        
        # draw a background
        self.screen.fill(pygame.Color(100, 100, 255, 255))


        # do stuff here
        self.test.update(event, self.screen)
        self.player.update(event, self.screen)

        pygame.display.update()

        # scale n display
        scaled_surface = pygame.transform.scale(self.screen, self.window_size)

        self.window.blit(scaled_surface, (0, 0))



