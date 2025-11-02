# testing state changes
import os

import pygame
import pygame.freetype

from ..config import *
from .state import State

class Blue(State):

    def __init__(self):
        self.count = 0

    def update(self, event: pygame.event.Event, screen: pygame.Surface, state_machine):


        self.count += 1

        if self.count >= 3 * FRAMES_PER_SECOND:
            state_machine.set_state("level")

        my_font = pygame.freetype.Font(os.path.join("assets", "fonts", "medodica.regular.otf"), 20)

        my_font.antialiased = False
        

        screen.fill((0,0,255))
        my_font.render_to(screen, (10,10), "testing scenes!!!", (255, 255, 255))



        

    def restart(self):
        pass