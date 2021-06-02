from constants import pygame, DISPLAY, FONT_TYPE, FONT_COLOR


class Record:
    """Class for adding, updating and sorting records.

        Attributes:
            rec_table: dictionary that stores names and records.
    """

    def __init__(self, table):
        """Initializes Record with table of records."""
        self.rec_table = table

    def update(self, name, score):
        """Adds a new record or updates an old one.
        Sorts in descending order and leaves the first 5 records.

        Args:
            name: player name.
            score: points scored per game.
        Returns:
            rec_table: dictionary that stores names and records.
        """
        if name not in self.rec_table or self.rec_table[name] < score:
            self.rec_table[name] = score

        sorted_values = sorted(self.rec_table.items(), key=lambda element: element[1])
        self.rec_table = dict(sorted_values[-5:])
        return self.rec_table

    def print_table(self, x, y):
        """Prints the high score table.

        Args:
            x: x coordinate of the first line of the record.
            y: y coordinate of the first line of the record.
        Returns:
            None.
        """
        step_x = 225
        step_y = 50
        font = pygame.font.Font(FONT_TYPE, 30)
        for name, score in reversed(self.rec_table.items()):
            name_text = font.render(name, True, FONT_COLOR)
            DISPLAY.blit(name_text, (x, y))
            x += step_x
            score_text = font.render(str(score), True, FONT_COLOR)
            DISPLAY.blit(score_text, (x, y))
            y += step_y
            x -= step_x

    def get_min_score(self):
        if len(self.rec_table) == 0:
            return 0
        sorted_values = sorted(self.rec_table.items(), key=lambda element: element[1])
        return sorted_values[0][1]
