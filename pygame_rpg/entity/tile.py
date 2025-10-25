import pygame

from .entity import Entity

class Tile(Entity):
    def __init__(self, x, y, img_path, img_x, img_y, collidable):
        super().__init__(x, y, img_path)

        self.collidable = collidable

        self.img = self.img.subsurface(img_x, img_y, 16, 16)

    def update(self, event, screen, camera):
        super().update(event, screen, camera)
        self.draw(screen)

