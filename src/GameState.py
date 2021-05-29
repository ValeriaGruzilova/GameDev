from enum import Enum


class State(Enum):
    MENU = 0,
    START = 1,
    SCORES_TABLE = 2,
    SCORES_TABLE_ENTER = 3,
    QUIT = 4


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
