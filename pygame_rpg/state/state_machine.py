import pygame

from .state import State

from .level import Level
from .blue import Blue
from .battle import Battle

class StateMachine():
    
    def __init__(self, starting_state: str):
        self.setup_states_dict()

        self.state = self.states[starting_state]

    def get_state(self) -> State: 
        return self.state
    
    def set_state(self, state):
        self.state = self.states[state]
        self.state.restart()

    def setup_states_dict(self):
        self.states = {
            "level": Level(),
            "blue": Blue(),
            "battle": Battle()
        }