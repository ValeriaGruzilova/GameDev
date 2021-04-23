import random
from constants import *
from Barrier import *

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

pygame.display.set_caption('Magic Drive')

pygame.mixer.music.load('assets/background/music.mp3')
pygame.mixer.music.set_volume(0.3)

pygame.display.set_icon(ICON)

scores = 0
max_scores = 0

health = 2


def run_game():
    pygame.mixer.music.play(-1)

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

        count_scores(barrier_arr)

        land_x -= 0.5  # движение фона
        x_rel = land_x % DISPLAY_WIDTH
        x_part2 = x_rel - DISPLAY_WIDTH if x_rel > 0 else x_rel + DISPLAY_WIDTH

        DISPLAY.blit(land, (x_rel, 0))
        DISPLAY.blit(land, (x_part2, 0))

        print_text("Score: " + str(scores), 20, 80, 45)

        draw_barrier_array(barrier_arr)  # движение барьеров

        draw_character(char_img_counter, usr_y)

        if check_collision(barrier_arr, usr_y):
            pygame.mixer.music.stop()
            print_text('GAME OVER. Press ENTER to RESTART', 110, 250, 50)
            print_text('Press ESC to EXIT', 240, 310, 50)
            game = False

        show_health()

        if keys[pygame.K_ESCAPE]:
            print_text('PAUSED. Press ENTER to CONTINUE', 130, 250, 50)
            pause()

        pygame.display.update()  # обновление дисплея
        CLOCK.tick(75)
    return not game_over()


def application():
    global scores
    global health
    while run_game():
        scores = 0
        health = 2
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
            radius += 250
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

    pygame.mixer.music.pause()

    while paused:
        for event in pygame.event.get():  # выход
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        CLOCK.tick(35)

    pygame.mixer.music.unpause()


def check_collision(barriers, usr_y):
    for barrier in barriers:
        if usr_y[0] + USR_HEIGHT >= barrier.y:
            if barrier.x <= USR_X <= barrier.x + barrier.width - 10:
                if check_health():
                    return_object(barriers, barrier)
                    return False
                else:
                    return True
            elif barrier.x <= USR_X + USR_WIDTH - 5 <= barrier.x + barrier.width - 5:
                if check_health():
                    return_object(barriers, barrier)
                    return False
                else:
                    return True
    return False


def game_over():
    # global scores, max_scores
    # if scores > max_scores:
    #    max_scores = scores

    stopped = True
    while stopped:
        for event in pygame.event.get():  # выход
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            restart()
            return False
        if keys[pygame.K_ESCAPE]:
            return True

        pygame.display.update()
        CLOCK.tick(35)


def restart():
    for i in range(90):
        if i <= 30:
            print_text('3..', 310, 150, 80)
        elif 30 < i <= 60:
            print_text('2..', 380, 150, 80)
        else:
            print_text('1..', 450, 150, 80)
        pygame.display.update()
        CLOCK.tick(25)


def count_scores(barriers):
    global scores
    for barrier in barriers:
        if barrier.x - 1 <= USR_X <= barrier.x + 2:
            scores += 1


def show_health():
    global health
    shown = 0
    coord = 20
    while shown != health:
        DISPLAY.blit(HEALTH_IMG, (coord, 20))
        coord += 55
        shown += 1


def check_health():
    global health
    health -= 1
    if health == 0:
        return False
    else:
        return True


def return_object(objects, obj):
    radius = find_radius(objects)

    choice = random.randrange(0, 3)
    img = BARRIER_IMG[choice]
    width = BARRIER_OPTIONS[choice][0]
    height = BARRIER_OPTIONS[choice][1]

    obj.return_self(radius, height, width, img)


application()
