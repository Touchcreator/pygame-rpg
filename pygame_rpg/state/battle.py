# rudimentary battle scene
# really just wanted to test how battles would yk work

import os
import colorsys

import pygame

from ..config import *
from ..util import *
from ..state import State


class Battle(State):

    def __init__(self):
        self.should_play = True # only for testing

        self.frame_count = 0

        self.players = ["nut"] # maybe there can be coop fight
        self.opponents = ["empty"] # ill add that later
        self.playerimg = pygame.image.load(os.path.join("assets", "img", "nutgun2.png"))
        self.enemyimg = pygame.image.load(os.path.join("assets", "img", "tochohalotest.png"))
        
        self.player_x = 0 - self.playerimg.width
        self.player_y = SCREEN_HEIGHT // 2 - self.playerimg.height // 2

        self.enemy_y = SCREEN_HEIGHT // 2 - self.enemyimg.height // 2

    def update(self, event: pygame.event.Event, screen: pygame.Surface, state_machine):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.should_play = False
            state_machine.set_state("level")

        if self.should_play:
            screen.fill(hsv_to_rgb(self.frame_count % 60 / 60, .5, .8))


            if self.frame_count <= FRAMES_PER_SECOND * 5:
                self.player_x += (35 - self.player_x) / 5
            else:
                self.player_x = 35

            screen.blit(self.playerimg, (round(self.player_x), self.player_y))
            screen.blit(self.enemyimg, (SCREEN_WIDTH - round(self.player_x) - self.enemyimg.width, self.enemy_y))

            self.frame_count+=1


        


        