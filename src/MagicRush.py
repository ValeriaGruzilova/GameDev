import random
from constants import *
from Object import *
from Button import *

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

pygame.display.set_caption('Magic Rush')

pygame.mixer.music.load('assets/background/music.mp3')
pygame.mixer.music.set_volume(0.2)

pygame.display.set_icon(ICON)

scores = 0
max_scores = 0

health = 2


def show_menu():
    show = True
    start_message = "START GAME"
    quit_message = "EXIT"

    start_button = Button(180, 55)
    quit_button = Button(110, 55)

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        DISPLAY.blit(MENU_BACKGR, (0, 0))
        start_button.draw(310, 320, start_message, launch_game)
        quit_button.draw(340, 420, quit_message, quit)

        pygame.display.update()
        CLOCK.tick(60)


def run_game():
    """Basic application function that calls helper functions and starts the main processes.

    Args:
        None.
    Returns:
        boolean value that means whether there is a signal from the user to end the game or not.
    """
    pygame.mixer.music.play(-1)

    game = True
    barrier_arr = []
    create_barrier_arr(barrier_arr)
    background = pygame.image.load('assets/background/backgr.png')
    background_x = 0

    make_jump = False
    usr_y = list()
    usr_y.append(PRIME_USR_Y)
    jump_counter = list()
    jump_counter.append(30)
    char_img_counter = list()
    char_img_counter.append(0)

    heart = Object(2 * DISPLAY_WIDTH, 360, 30, HEALTH_MINI_IMG, 4)

    while game:
        change_speed(barrier_arr, heart)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            make_jump = True

        if make_jump:
            make_jump = jump(make_jump, usr_y, jump_counter)

        count_scores(barrier_arr)

        background_x -= 0.5  # background movement
        x_rel = background_x % DISPLAY_WIDTH
        x_part2 = x_rel - DISPLAY_WIDTH if x_rel > 0 else x_rel + DISPLAY_WIDTH

        DISPLAY.blit(background, (x_rel, 0))
        DISPLAY.blit(background, (x_part2, 0))

        print_text("Score: " + str(scores), 20, 80, 45)

        draw_barrier_array(barrier_arr)  # barriers` movement

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

        heart.move()
        hearts_plus(heart, usr_y)

        pygame.display.update()
        CLOCK.tick(75)
    return not game_over()


def launch_game():
    """Launches the game and updates the points and health of the character with each restart.

    Args:
        None.
    Returns:
        None.
    """
    global scores
    global health

    while run_game():
        scores = 0
        health = 2

    scores = 0
    health = 2

    show_menu()
    # pygame.quit()
    # quit()


def jump(make_jump, usr_y, jump_counter):
    """Moves the character up and down on the y-axis to create the illusion of a jump.

    Args:
        make_jump: boolean value about the need to jump.
        usr_y: user y coordinate.
        jump_counter: counter displacement of the character during a jump.
    Returns:
        make_jump: boolean value about the need to jump.
    """
    if jump_counter[0] >= -30:
        usr_y[0] -= jump_counter[0] / 4.0
        jump_counter[0] -= 1
    else:
        jump_counter[0] = 30
        make_jump = not make_jump

    return make_jump


def create_barrier_arr(array):
    """Creates and initializes an array of 3 random barrier objects.

    Args:
        array: array of barrier objects.
    Returns:
        None.
    """
    change_pos = 20
    for i in range(3):
        choice = random.randrange(0, 3)
        img = BARRIER_IMG[choice]
        width = BARRIER_OPTIONS[choice][0]
        height = BARRIER_OPTIONS[choice][1]
        array.append(Object(DISPLAY_WIDTH + change_pos, height, width, img, 4))
        change_pos += 300


def find_radius(array):
    """Generates a radius of far or near placement of barriers.

    Args:
        array: array of barrier objects.
    Returns:
        radius: integer value of the new coordinate of the object.
    """
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
    """If the object is outside the display boundary, a new random object is drawn with a new spawn radius.

    Args:
        array: array of barrier objects.
    Returns:
        None.
    """
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
    """Draws animation of the character's movement and jumping (phase change).

    Args:
        img_counter: character animation counter.
        usr_y: user y coordinate.
    Returns:
        None.
    """
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
    """Pauses the game and music, waits for a signal from the user to continue the game.

    Args:
        None.
    Returns:
        None.
    """
    paused = True

    pygame.mixer.music.pause()

    while paused:
        for event in pygame.event.get():
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
    """When the character object and the barrier object collides, checks the presence of health.

    Args:
        barriers: array of barrier objects.
        usr_y: user y coordinate.
    Returns:
        boolean value indicating whether there was a fatal collision.
    """
    for barrier in barriers:
        if usr_y[0] + USR_HEIGHT >= barrier.y:
            if barrier.x <= USR_X <= barrier.x + barrier.width - 10:
                if check_health():
                    return_barrier(barriers, barrier)
                    return False
                else:
                    return True
            elif barrier.x <= USR_X + USR_WIDTH - 5 <= barrier.x + barrier.width - 5:
                if check_health():
                    return_barrier(barriers, barrier)
                    return False
                else:
                    return True
    return False


def game_over():
    """Depending on the user's choice, starts the restart or the end of the game.

    Args:
        None.
    Returns:
        boolean value that means whether there is a signal from the user to end the game or not.
    """
    # global scores, max_scores
    # if scores > max_scores:
    #    max_scores = scores

    stopped = True
    while stopped:
        for event in pygame.event.get():
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
        if barrier.x - barrier.speed + 3 <= USR_X <= barrier.x + barrier.speed - 2:
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


def return_barrier(barriers, barr):
    """Returns a random barrier object to a new coordinate.

    Args:
        barriers: array of barrier objects.
        barr: barrier object.
    Returns:
        None.
    """
    radius = find_radius(barriers)

    choice = random.randrange(0, 3)
    img = BARRIER_IMG[choice]
    width = BARRIER_OPTIONS[choice][0]
    height = BARRIER_OPTIONS[choice][1]

    barr.return_self(radius, height, width, img)


def hearts_plus(heart, usr_y):
    """When a character catches a heart, increases health and returns the heart object to a new coordinate.

    Args:
        heart: character health object.
        usr_y: user y coordinate.
    Returns:
        None.
    """
    global health
    if heart.x <= -heart.width:
        radius = DISPLAY_WIDTH + random.randrange(2000, 3700)
        heart.return_self(radius, heart.y, heart.width, heart.image)

    if USR_X <= heart.x <= USR_X + USR_WIDTH:
        if usr_y[0] <= heart.y <= usr_y[0] + USR_HEIGHT:
            if health < 3:
                health += 1

            radius = DISPLAY_WIDTH + random.randrange(3000, 4700)
            heart.return_self(radius, heart.y, heart.width, heart.image)


def change_speed(barriers, heart):
    """Increases the speed of barriers and hearts every 20 points and calls the setter.

    Args:
        barriers: array of barrier objects.
        heart: character health object.
    Returns:
        None.
    """
    global scores
    new_speed = scores // 20 / 4 + 4
    for barrier in barriers:
        barrier.set_speed(new_speed)
    heart.set_speed(new_speed)


show_menu()
# launch_app()
