import pygame
import random

pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Magic Drive')

icon = pygame.image.load('background/icon.jpg')
pygame.display.set_icon(icon)


class Barrier:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move(self):
        if self.x >= self.width - 100:
            pygame.draw.rect(display, (224, 121, 31), (self.x, self.y, self.width, self.height))
            self.x -= self.speed
            return True
        else:
            return False

    def return_self(self, radius):
        self.x = radius


usr_width = 100
usr_height = 80
usr_x = display_width // 3
usr_y = display_height - usr_height - 82

barrier_width = 20
barrier_height = 70
barrier_x = display_width - 50
barrier_y = display_height - barrier_height - 82

clock = pygame.time.Clock()

make_jump = False
jump_counter = 30


def run_game():
    global make_jump
    game = True
    barrier_arr = []
    create_barrier_arr(barrier_arr)
    land = pygame.image.load(r'background/backgr.png')
    land_x = 0

    while game:
        for event in pygame.event.get():  # выход
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()  # прыжок
        if keys[pygame.K_SPACE]:
            make_jump = True

        if make_jump:
            jump()

        land_x -= 0.5  # движение фона
        x_rel = land_x % display_width
        x_part2 = x_rel - display_width if x_rel > 0 else x_rel + display_width

        display.blit(land, (x_rel, 0))
        display.blit(land, (x_part2, 0))

        draw_array(barrier_arr)  # движение барьеров

        pygame.draw.rect(display, (247, 240, 22), (usr_x, usr_y, usr_width, usr_height))  # персонаж

        pygame.display.update()  # обновление дисплея
        clock.tick(80)


def jump():
    global usr_y, jump_counter, make_jump
    if jump_counter >= -30:
        usr_y -= jump_counter / 2.5
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = False


def create_barrier_arr(array):
    array.append(Barrier(display_width + 20, display_height - 152, 30, 70, 4))
    array.append(Barrier(display_width + 300, display_height - 132, 40, 50, 4))
    array.append(Barrier(display_width + 600, display_height - 112, 70, 30, 4))


def find_radius(array):
    maximum = max(array[0].x, array[1].x, array[2].x)

    if maximum < display_width:
        radius = display_width
        if radius - maximum < 70:
            radius += 150
    else:
        radius = maximum

    choice = random.randrange(0, 5)
    if choice == 0:
        radius += random.randrange(10, 15)
    else:
        radius += random.randrange(230, 380)

    return radius


def draw_array(array):
    for barrier in array:
        check = barrier.move()
        if not check:
            radius = find_radius(array)
            barrier.return_self(radius)


run_game()