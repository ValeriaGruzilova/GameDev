from constants import pygame, DISPLAY, FONT_TYPE, FONT_COLOR


class Button:
    """Class for representing objects.

        Attributes:
            width: button width.
            height: button height.
            inactive_color: rgb-code of inactive button`s color.
            active_color: rgb-code of active button`s color.
    """

    def __init__(self, width, height):
        """Initializes Button with button width, button height, inactive and active colors."""
        self.width = width
        self.height = height
        self.inactive_color = (232, 250, 255)
        self.active_color = (164, 229, 245)

    def draw(self, x_btn, y_btn, message, action=None):
        """Draws the button, reacts to mouse actions and calls the method for printing text.

        Args:
            x_btn: the x coordinate of the button relative to the display.
            y_btn: the y coordinate of the button relative to the display.
            message: button message.
            action: the function that is called when the button is clicked.
        Returns:
            None.
        """
        mouse_coord = pygame.mouse.get_pos()
        # mouse_coord[0] = x; mouse_coord[1] = y
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(DISPLAY, self.inactive_color, (x_btn, y_btn, self.width, self.height))
        if x_btn < mouse_coord[0] < x_btn + self.width:
            if y_btn < mouse_coord[1] < y_btn + self.height:
                pygame.draw.rect(DISPLAY, self.active_color, (x_btn, y_btn, self.width, self.height))

                if click[0] == 1:
                    # click[0] = left mouse button pressed
                    pygame.time.delay(300)
                    if action is not None:
                        # if action == quit:
                        #    pygame.quit()
                        #    quit()
                        action()
                    else:
                        return True

        self.print_text(message, x_btn, y_btn, 30)

    def print_text(self, message, x_btn, y_btn, font_size):
        """Prints the message text in the center of the button.

        Args:
            message: button message.
            x_btn: the x coordinate of the button relative to the display.
            y_btn: the y coordinate of the button relative to the display.
            font_size: button message font size.
        Returns:
            None.
        """
        x_text = x_btn + self.width / 2 - len(message) * 12 / 2
        y_text = y_btn + 14
        font = pygame.font.Font(FONT_TYPE, font_size)
        text = font.render(message, True, FONT_COLOR)
        DISPLAY.blit(text, (x_text, y_text))
