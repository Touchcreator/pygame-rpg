import os

import pygame

from ..map_loader import MapLoader
from ..config import *
from ..entity import *

from .state import State

class Level(State):
    def __init__(self):
        tiles = MapLoader.load(os.path.join("assets", "maps", "map1.txt"))
        self.tiles_obj = []
        self.collidable_tiles = []
        self.changed_scene = False


        # TODO: make a list of entities like most games

        # make all tiles (soon ill add clipping
        tilex = 0
        tiley = 0

        i = 0
        j = 0
        while i < len(tiles):
            while j < len(tiles[1]):
                collidable = False
                if tiles[i][j] == "1":
                    collidable = True


                to_append = Tile(j * TILESIZE, i * TILESIZE, TILES_PATH, int(tiles[i][j]) * 16, 0, collidable)

                self.tiles_obj.append(to_append)
                j += 1

            i += 1
            j = 0

        for tiles in self.tiles_obj:
            if tiles.collidable:
                self.collidable_tiles.append(tiles)

        self.test = Entity(7 * TILESIZE, 9 * TILESIZE, os.path.join("assets", "img", "nutstill.png"))

        self.player = Player(TILESIZE * 6, TILESIZE * 7, NUT_ASSETS)
        
        running = True

    def update(self, event: pygame.event.Event, screen: pygame.Surface, state_machine):
        # draw a background
        screen.fill(pygame.Color(100, 100, 255, 255))


        # do stuff here

        for tile in self.tiles_obj:
            tile.update(event, screen, (self.player.x, self.player.y))
            

        self.test.update(event, screen, (self.player.x, self.player.y))
        self.player.update(event, screen, self.collidable_tiles)

        # ordered drawing
        sprites = [self.test, self.player]

        sprites.sort(key=lambda y: y.y)

        for sprite in sprites:
            sprite.draw(screen)

        if self.player.x > 200 and not self.changed_scene:
            state_machine.set_state("battle")
            self.changed_scene = True

        
            

    def restart(self):
        pass