from constants import DISPLAY


class Barrier:
    def __init__(self, x, y, width, image, speed):
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.speed = speed

    def move(self):
        if self.x >= self.width - 100:
            DISPLAY.blit(self.image, (self.x, self.y))
            self.x -= self.speed
            return True
        else:
            return False

    def return_self(self, radius, y, width, image):
        self.x = radius
        self.y = y
        self.width = width
        self.image = image
        DISPLAY.blit(self.image, (self.x, self.y))
