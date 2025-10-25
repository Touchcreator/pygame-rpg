import pygame

from ..config import *

class Entity:

    def __init__(self, x, y, img_path):
        self.x = x
        self.y = y
        self.img: pygame.Surface = pygame.image.load(img_path).convert_alpha()

    def update(self, event, screen: pygame.Surface, camera: tuple):
        global displayx, displayy

        # update code here


        # draw code here

        displayx = self.x - camera[0] -8 + SCREEN_WIDTH / 2
        displayy = self.y - camera[1] -8 + SCREEN_HEIGHT / 2

        

    def draw(self, screen):
        if (displayx >= -16 and displayx <= SCREEN_WIDTH) and (displayy >= -16 and displayy <= SCREEN_HEIGHT):
            screen.blit(self.img, (displayx, displayy))