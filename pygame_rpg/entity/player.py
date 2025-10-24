import pygame

from .entity import Entity

# TODO: add animation support

class Player(Entity):

    def __init__(self, x, y, img_path):
        super().__init__(x, y, img_path)
        self.speed = 2

    def update(self, event, screen: pygame.Surface):

        keys = pygame.key.get_pressed()

        # update code here
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

                

        #self.x += 4

        # draw code here

        screen.blit(self.img, (self.x, self.y))