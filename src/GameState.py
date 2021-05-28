from enum import Enum


class State(Enum):
    MENU = 0,
    START = 1,
    QUIT = 2


class GameState:
    """Class for setting state values.

        Attributes:
            state: name of the state, which will then call the corresponding function.
    """

    def __init__(self):
        """Initializes GameState with state value MENU."""
        self.state = State.MENU

    def set_state(self, state):
        self.state = state
