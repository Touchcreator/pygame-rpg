import pygame

class State():

    def __init__(self):
        print(self.__class__.__name__ + ": forgot to override the init function!")


    def update(self, event: pygame.event.Event, screen: pygame.Surface, state_machine):
        print(self.__class__.__name__ + ": forgot to override the update function!")


    def restart(self):
        print(self.__class__.__name__ + ": no restart function, using __init__")
        self.__init__()