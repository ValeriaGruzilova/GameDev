from constants import DISPLAY


class Object:
    """Class for representing objects.

        Attributes:
            x: the x coordinate of the object relative to the display.
            y: the y coordinate of the object relative to the display.
            width: object image width.
            image: picture of the object shown on the display.
            speed: object movement speed.
    """

    def __init__(self, x, y, width, image, speed):
        """Initializes Object with x, y coordinates, object width, image and speed."""
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.speed = speed

    def move(self):
        """Checks if the object is shown on the display.
        If yes, then draws its movement at a given speed in the horizontal direction.

        Args:
            None.
        Returns:
            Boolean value indicating whether the object is on the display.
        """
        if self.x >= self.width - 100:
            DISPLAY.blit(self.image, (self.x, self.y))
            self.x -= self.speed
            return True
        else:
            return False

    def return_self(self, radius, y, width, image):
        """Returns the object to the new given radius and draws it there.

        Args:
            radius: radius of movement of the object.
            y: the y coordinate of the object relative to the display.
            width: object image width.
            image: picture of the object shown on the display.
        Returns:
            None.
        """
        self.x = radius
        self.y = y
        self.width = width
        self.image = image
        DISPLAY.blit(self.image, (self.x, self.y))

    def set_speed(self, speed):
        self.speed = speed
