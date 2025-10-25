import pygame

from .entity import Entity

from ..config import *

# TODO: add animation support

box_x = 0
box_y = 0

# WARNING!!!
# i spent hours on the collision code; its ass.
# it works but i had to come up w crazy shortcuts bro
# its held together by paper clips
# like it looks simple but as soon as u change one thing, it all messes up
# anyway, have fun! :3

key_down = False
key_down_before = False

class Player(Entity):

    def __init__(self, x, y, img_path):
        super().__init__(x, y, "assets/img/nutv2.png")
        self.speed = 1

        self.col_box_x = 3
        self.col_box_y = 11
        self.col_box_w = 10
        self.col_box_h = 5

        self.direction = "down"
        self.frame = 0

        self.frame_count = 0



    def update(self, event, screen: pygame.Surface, tiles_list):
        global key_down, key_down_before

        if self.frame_count % 5 == 0:
            self.frame += 1
        if self.frame > 3:
            self.frame = 0

        if not key_down:
            self.frame = 0

        self.frame_count += 1

        global box_y, box_x
        self.update_box_pos()

        keys = pygame.key.get_pressed()

        tiles_collied = 0

        key_down_before = key_down

        # update code here
        if keys[pygame.K_UP]:
            key_down = True
            self.set_direction("up")
            self.y -= self.speed

            for tile in tiles_list: # down collsion

                if tile.y + 16 < box_y + self.col_box_h - 1 and tile.y + 16 > box_y - 1:
                    if tile.x < box_x + self.col_box_w and tile.x + 16 > box_x:
                        tiles_collied += 1
                        
            if tiles_collied:
                self.y += self.speed

            

        elif keys[pygame.K_LEFT]:
            key_down = True
            self.set_direction("left")
            self.x -= self.speed

            for tile in tiles_list: # left collsion

                if tile.x + 16 > box_x - 1 and tile.x + 16 < box_x + self.col_box_w + 1:
                    if tile.y < box_y + self.col_box_h and tile.y + 16 > box_y:
                        tiles_collied += 1

            if tiles_collied:
                self.x += self.speed

        elif keys[pygame.K_RIGHT]:
            key_down = True
            self.set_direction("right")
            self.x += self.speed

            for tile in tiles_list: # right collsion

                if tile.x < box_x + self.col_box_w +1 and tile.x > box_x -1:
                    if tile.y < box_y + self.col_box_h and tile.y + 16 > box_y :
                        tiles_collied += 1
                        
            if tiles_collied:
                self.x -= self.speed

        elif keys[pygame.K_DOWN]:
            key_down = True
            self.set_direction("down")
            self.y += self.speed

            for tile in tiles_list: # down collsion

                if tile.y < box_y + self.col_box_h + 1 and tile.y > box_y + 1:
                    if tile.x < box_x + self.col_box_w and tile.x + 16 > box_x:
                        tiles_collied += 1
                        
            if tiles_collied:
                self.y -= self.speed

        else:
            key_down = False
                        

                

        # getting the right pixels for img
        row = 0

        if self.direction == "down":
            row = 0
        elif self.direction == "up":
            row = 1
        elif self.direction == "right":
            row = 2
        else:
            row = 3

        column = self.frame

        if not key_down_before and key_down:
            self.frame = 1

        # draw code here

        new = self.img.subsurface(column * 16, row * 16, 16, 16)
        

        screen.blit(new, (-8 + SCREEN_WIDTH / 2, -8 + SCREEN_HEIGHT / 2))

    def update_box_pos(self):
        global box_y, box_x
        box_x = self.x + self.col_box_x
        box_y = self.y + self.col_box_y

    def set_direction(self, direction):
        if self.direction != direction:
            self.direction = direction
            