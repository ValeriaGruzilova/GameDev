from constants import pygame, DISPLAY, FONT_TYPE, FONT_COLOR


class Record:
    def __init__(self, table):
        self.rec_table = table

    def update(self, name, score):
        if name not in self.rec_table or self.rec_table[name] < score:
            self.rec_table[name] = score

        sorted_values = sorted(self.rec_table.items(), key=lambda element: element[1])
        self.rec_table = dict(sorted_values[-5:])
        return self.rec_table

    def print_table(self, x, y):
        step_x = 240
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
