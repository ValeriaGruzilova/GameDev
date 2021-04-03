import random
from constants import *
from Barrier import *

pygame.init()

pygame.display.set_caption('Magic Drive')

pygame.display.set_icon(ICON)


def run_game():
    game = True
    barrier_arr = []
    create_barrier_arr(barrier_arr)
    land = pygame.image.load(r'src/background/backgr.png')
    land_x = 0

    make_jump = False
    usr_y = list()
    usr_y.append(DISPLAY_HEIGHT - USR_HEIGHT - 82)
    jump_counter = list()
    jump_counter.append(30)

    while game:
        for event in pygame.event.get():  # выход
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()  # прыжок
        if keys[pygame.K_SPACE]:
            make_jump = True

        if make_jump:
            make_jump = jump(make_jump, usr_y, jump_counter)

        land_x -= 0.5  # движение фона
        x_rel = land_x % DISPLAY_WIDTH
        x_part2 = x_rel - DISPLAY_WIDTH if x_rel > 0 else x_rel + DISPLAY_WIDTH

        DISPLAY.blit(land, (x_rel, 0))
        DISPLAY.blit(land, (x_part2, 0))

        draw_array(barrier_arr)  # движение барьеров

        pygame.draw.rect(DISPLAY, (247, 240, 22), (USR_X, usr_y[0], USR_WIDTH, USR_HEIGHT))  # персонаж

        pygame.display.update()  # обновление дисплея
        CLOCK.tick(75)


def jump(make_jump, usr_y, jump_counter):
    if jump_counter[0] >= -30:
        usr_y[0] -= jump_counter[0] / 2.75
        jump_counter[0] -= 1
    else:
        jump_counter[0] = 30
        make_jump = not make_jump

    return make_jump


def create_barrier_arr(array):
    change_pos = 20
    for i in range(3):
        choice = random.randrange(0, 3)
        img = BARRIER_IMG[choice]
        width = BARRIER_OPTIONS[choice][0]
        height = BARRIER_OPTIONS[choice][1]
        array.append(Barrier(DISPLAY_WIDTH + change_pos, height, width, img, 4))
        change_pos += 300


def find_radius(array):
    maximum = max(array[0].x, array[1].x, array[2].x)

    if maximum < DISPLAY_WIDTH:
        radius = DISPLAY_WIDTH
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

            choice = random.randrange(0, 3)
            img = BARRIER_IMG[choice]
            width = BARRIER_OPTIONS[choice][0]
            height = BARRIER_OPTIONS[choice][1]

            barrier.return_self(radius, height, width, img)


run_game()
