import pygame

from .config import *

from .entity import *

from .settings import Settings
from .map_loader import MapLoader

class Game:

    def __init__(self):

        # set up settings
        self.settings = Settings()
        scale = self.settings.data["scale"]

        pygame.init()
        game_size = width, height = SCREEN_WIDTH, SCREEN_HEIGHT
        self.window_size = width, height = round(160 * scale), round(120 * scale) # this will be based on ur settings, gotta add an editor tho

        self.screen = pygame.Surface(game_size) # the game
        self.window = pygame.display.set_mode(self.window_size) # and scaled ggame

        pygame.display.set_caption("Nut Simulator: He Returns...")

        self.clock = pygame.time.Clock()

        

    def run(self):

        tiles = MapLoader.load("assets/maps/map1.txt")
        self.tiles_obj = []
        self.collidable_tiles = []


        # TODO: make a list of entities like most games

        # make all tiles (soon ill add clipping
        tilex = 0
        tiley = 0

        i = 0
        j = 0
        while i < len(tiles):
            while j < len(tiles[1]):
                to_append = Tile(j * TILESIZE, i * TILESIZE, TILES_PATH, int(tiles[i][j]) * 16, 0, False)

                if tiles[i][j] == 1:
                    to_append.collidable = True
                    self.collidable_tiles.append(to_append)

                self.tiles_obj.append(to_append)
                j += 1

            i += 1
            j = 0

            


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

        for tile in self.tiles_obj:
            tile.update(event, self.screen, (self.player.x, self.player.y))

        self.test.update(event, self.screen, (self.player.x, self.player.y))
        self.player.update(event, self.screen, self.collidable_tiles)
            
        

        pygame.display.update()

        # scale n display
        scaled_surface = pygame.transform.scale(self.screen, self.window_size)

        self.window.blit(scaled_surface, (0, 0))



