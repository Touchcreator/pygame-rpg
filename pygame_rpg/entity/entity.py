import pygame

from ..config import *

class Entity:

    def __init__(self, x, y, img_path):
        self.x = x
        self.y = y
        self.img: pygame.Surface = pygame.image.load(img_path).convert_alpha()

    def update(self, event, screen: pygame.Surface, camera: tuple):

        # update code here


        # draw code here

        screen.blit(self.img, (self.x - camera[0] -8 + SCREEN_WIDTH / 2, self.y - camera[1] -8 + SCREEN_HEIGHT / 2))

