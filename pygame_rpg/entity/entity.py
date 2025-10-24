import pygame

class Entity:

    def __init__(self, x, y, img_path):
        self.x = x
        self.y = y
        self.img = pygame.image.load(img_path).convert_alpha()

    def update(self, event, screen: pygame.Surface):

        # update code here


        # draw code here

        screen.blit(self.img, (self.x, self.y))

