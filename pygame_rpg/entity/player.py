import pygame

from .entity import Entity

from ..config import *

# TODO: add animation support

box_x = 0
box_y = 0

# WARNING!!!
# i spent hours on the collision code; its ass.
# idek if god knows how these collisions work
# its held together by paper clips
# have fun! :3

class Player(Entity):

    def __init__(self, x, y, img_path):
        super().__init__(x, y, img_path)
        self.speed = 1

        self.col_box_x = 3
        self.col_box_y = 11
        self.col_box_w = 10
        self.col_box_h = 5



    def update(self, event, screen: pygame.Surface, tiles_list):

        global box_y, box_x
        self.update_box_pos()

        keys = pygame.key.get_pressed()

        tiles_collied = 0

        # update code here
        if keys[pygame.K_UP]:
            self.y -= self.speed

            for tile in tiles_list: # down collsion

                if tile.y + 16 < box_y + self.col_box_h - 1 and tile.y + 16 > box_y - 1:
                    if tile.x < box_x + self.col_box_w and tile.x + 16 > box_x:
                        tiles_collied += 1
                        
            if tiles_collied:
                self.y += self.speed

            

        elif keys[pygame.K_LEFT]:
            self.x -= self.speed

            for tile in tiles_list: # left collsion

                if tile.x + 16 > box_x - 1 and tile.x + 16 < box_x + self.col_box_w + 1:
                    if tile.y < box_y + self.col_box_h and tile.y + 16 > box_y:
                        tiles_collied += 1

            if tiles_collied:
                self.x += self.speed

        elif keys[pygame.K_RIGHT]:
            self.x += self.speed

            for tile in tiles_list: # right collsion

                if tile.x < box_x + self.col_box_w +1 and tile.x > box_x -1:
                    if tile.y < box_y + self.col_box_h and tile.y + 16 > box_y :
                        tiles_collied += 1
                        
            if tiles_collied:
                self.x -= self.speed

        elif keys[pygame.K_DOWN]:
            self.y += self.speed

            for tile in tiles_list: # down collsion

                if tile.y < box_y + self.col_box_h + 1 and tile.y > box_y + 1:
                    if tile.x < box_x + self.col_box_w and tile.x + 16 > box_x:
                        tiles_collied += 1
                        
            if tiles_collied:
                self.y -= self.speed
                        

                

        #self.x += 4

        # draw code here

        screen.blit(self.img, (-8 + SCREEN_WIDTH / 2, -8 + SCREEN_HEIGHT / 2))

    def update_box_pos(self):
        global box_y, box_x
        box_x = self.x + self.col_box_x
        box_y = self.y + self.col_box_y