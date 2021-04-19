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
    land = pygame.image.load('assets/background/backgr.png')
    land_x = 0

    make_jump = False
    usr_y = list()
    usr_y.append(PRIME_USR_Y)
    jump_counter = list()
    jump_counter.append(30)
    char_img_counter = list()
    char_img_counter.append(0)

    while game:
        for event in pygame.event.get():  # выход
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            make_jump = True

        if make_jump:
            make_jump = jump(make_jump, usr_y, jump_counter)

        land_x -= 0.5  # движение фона
        x_rel = land_x % DISPLAY_WIDTH
        x_part2 = x_rel - DISPLAY_WIDTH if x_rel > 0 else x_rel + DISPLAY_WIDTH

        DISPLAY.blit(land, (x_rel, 0))
        DISPLAY.blit(land, (x_part2, 0))

        draw_barrier_array(barrier_arr)  # движение барьеров

        draw_character(char_img_counter, usr_y)

        if check_collision(barrier_arr, usr_y):
            game = False

        if keys[pygame.K_ESCAPE]:
            pause()

        pygame.display.update()  # обновление дисплея
        CLOCK.tick(75)
    return not game_over()


def application():
    while run_game():
        pass
    pygame.quit()
    quit()


def jump(make_jump, usr_y, jump_counter):
    if jump_counter[0] >= -30:
        usr_y[0] -= jump_counter[0] / 4.0
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


def draw_barrier_array(array):
    for barrier in array:
        check = barrier.move()
        if not check:
            radius = find_radius(array)

            choice = random.randrange(0, 3)
            img = BARRIER_IMG[choice]
            width = BARRIER_OPTIONS[choice][0]
            height = BARRIER_OPTIONS[choice][1]

            barrier.return_self(radius, height, width, img)


def draw_character(img_counter, usr_y):
    if img_counter[0] == 39:
        img_counter[0] = 0

    if usr_y[0] == PRIME_USR_Y:
        img_counter[0] += 1
    else:
        img_counter[0] = 16

    DISPLAY.blit(WIZARD_IMG[img_counter[0] // 10], (USR_X, usr_y[0]))


def print_text(message, x, y, font_size):
    font = pygame.font.Font(FONT_TYPE, font_size)
    text = font.render(message, True, FONT_COLOR)
    DISPLAY.blit(text, (x, y))


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():  # выход
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text('PAUSED. Press ENTER to CONTINUE', 150, 250, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        CLOCK.tick(15)


def check_collision(barriers, usr_y):
    for barrier in barriers:
        if usr_y[0] + USR_HEIGHT >= barrier.y:
            if barrier.x <= USR_X <= barrier.x + barrier.width - 10:
                return True
            elif barrier.x <= USR_X + USR_WIDTH - 5 <= barrier.x + barrier.width - 5:
                return True
    return False


def game_over():
    stopped = True
    while stopped:
        for event in pygame.event.get():  # выход
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text('GAME OVER. Press ENTER to RESTART', 130, 250, 40)
        print_text('Press ESC to EXIT', 260, 310, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            restart()
            return False
        if keys[pygame.K_ESCAPE]:
            return True

        pygame.display.update()
        CLOCK.tick(15)


def restart():
    for i in range(60):
        if i <= 20:
            print_text('3..', 260, 150, 100)
        elif 20 < i <= 40:
            print_text('2..', 360, 150, 100)
        else:
            print_text('1..', 460, 150, 100)
        pygame.display.update()
        CLOCK.tick(15)


application()
