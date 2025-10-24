import pygame

from .entity import Entity

from ..config import *

# TODO: add animation support

class Player(Entity):

    def __init__(self, x, y, img_path):
        super().__init__(x, y, img_path)
        self.speed = 1

    def update(self, event, screen: pygame.Surface, tiles_list):

        keys = pygame.key.get_pressed()

        # update code here
        if keys[pygame.K_UP]:
            self.y -= self.speed

            
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_LEFT]:
            self.x -= self.speed

            for tile in tiles_list: # left collsion
                if tile.x + 16 <= self.x:
                    self.speed = 0
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

                

        #self.x += 4

        # draw code here

        screen.blit(self.img, (-8 + SCREEN_WIDTH / 2, -8 + SCREEN_HEIGHT / 2))