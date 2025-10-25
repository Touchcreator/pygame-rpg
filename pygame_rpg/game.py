import pygame

from .config import *

from .entity import *

from .settings import Settings
from .map_loader import MapLoader

from .state import *



class Game:

    def __init__(self):
        
        

        # set up settings
        self.settings = Settings()
        scale = self.settings.data["scale"]

        pygame.init()
        pygame.freetype.init() #initalizing fonts for stuff
        game_size = width, height = SCREEN_WIDTH, SCREEN_HEIGHT
        self.window_size = width, height = round(160 * scale), round(120 * scale) # this will be based on ur settings, gotta add an editor tho

        self.screen = pygame.Surface(game_size) # the game
        self.window = pygame.display.set_mode(self.window_size) # and scaled ggame

        pygame.display.set_caption("Nut Simulator: He Returns...")

        self.clock = pygame.time.Clock()

        # initialize state AFTER all pygame setup
        self.state_machine = StateMachine("level")
        

        

    def run(self):
        running = True
        

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # if it quits running is false
                    running = False

            self.clock.tick(FRAMES_PER_SECOND)

            self.update(event) # pass events into running which should be passed into objects n stuff

            

    def update(self, event):
        
        self.state_machine.get_state().update(event, self.screen, self.state_machine)

        pygame.display.update()

        # scale n display
        scaled_surface = pygame.transform.scale(self.screen, self.window_size)

        self.window.blit(scaled_surface, (0, 0))



