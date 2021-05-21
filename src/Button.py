from constants import pygame, DISPLAY, FONT_TYPE, FONT_COLOR


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (232, 250, 255)
        self.active_color = (164, 229, 245)

    def draw(self, x, y, message, action=None):
        mouse_coord = pygame.mouse.get_pos()  # mouse_coord[0] = x; mouse_coord[1] = y
        click = pygame.mouse.get_pressed()  # click[0] = left mouse button pressed
        pygame.draw.rect(DISPLAY, self.inactive_color, (x, y, self.width, self.height))
        if x < mouse_coord[0] < x + self.width:
            if y < mouse_coord[1] < y + self.height:
                pygame.draw.rect(DISPLAY, self.active_color, (x, y, self.width, self.height))

                if click[0] == 1:
                    pygame.time.delay(300)
                    if action is not None:
                        if action == quit:
                            pygame.quit()
                            quit()
                        action()

        self.print_text(message, x + self.width / 2 - len(message) * 12 / 2, y + 14, 30)

    @staticmethod
    def print_text(message, x, y, font_size):
        font = pygame.font.Font(FONT_TYPE, font_size)
        text = font.render(message, True, FONT_COLOR)
        DISPLAY.blit(text, (x, y))
