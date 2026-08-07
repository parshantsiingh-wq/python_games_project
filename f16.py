import pygame
import random
import os

pygame.init()

screen_width = 1200
screen_height = 600

# Background Image
# bg_image = pygame.image.load("sound/image_1.jpg")
# bg_image = pygame.transform.scale(bg_image, (screen_width, screen_height))
#
pygame.mixer.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


# ---------------- Functions ----------------

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, (x, y))


def plot_snake(game_window, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])
    if snk_list:
        head_x, head_y = snk_list[-1]
        pygame.draw.rect(game_window, (0, 100, 0), [head_x, head_y, snake_size, snake_size])

def welcome():
    exit_game = False

    while not exit_game:
        game_window.fill(white)

        text_screen("Welcome to Snake Game", black, 300, 220)
        text_screen("Press SPACE to Play", black, 350, 280)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("sound/gamemusic1.mp3")
                    pygame.mixer.music.play(-1)
                    game_loop()

        clock.tick(60)


# ---------------- Game Loop ----------------

def game_loop():

    # Check if hiscore file exists
    if not os.path.exists("f1.txt"):
        with open("f1.txt", "w") as f:
            f.write("0")

    snk_list = []
    snk_length = 1

    exit_game = False
    game_over = False

    snake_x = 45
    snake_y = 55

    snake_size = 15

    velocity_x = 0
    velocity_y = 0

    init_velocity = 5
    fps = 40

    score = 0

    with open("f1.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(20, screen_width - 20)
    food_y = random.randint(20, screen_height - 20)

    while not exit_game:

        if game_over:

            with open("f1.txt", "w") as f:
                f.write(str(hiscore))

            game_window.fill(white)
            text_screen("Game Over! Press ENTER to Continue", red, 150, 250)

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return game_loop()

        else:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 50

            snake_x += velocity_x
            snake_y += velocity_y

            # Food Collision
            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 10

                # pygame.mixer.music.load("sound/audio1.mp3")
                # pygame.mixer.music.play()

                food_x = random.randint(20, screen_width - 20)
                food_y = random.randint(20, screen_height - 20)

                if score > int(hiscore):
                    hiscore = score

                snk_length += 5

            # # Background
            # game_window.blit(bg_image, (0, 0))

            text_screen("Score :  " + str(score), red, 5, 5)
            text_screen("hiscore : " + str(hiscore), (255, 255, 0), 930, 5)

            pygame.draw.rect(
                game_window,
                red,
                [food_x, food_y, snake_size, snake_size],
            )

            head = [snake_x, snake_y]

            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            # Snake Collision
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("sound/gameover2.mp3")
                pygame.mixer.music.play()

            # Wall Collision
            if (
                snake_x < 0
                or snake_x > screen_width - snake_size
                or snake_y < 0
                or snake_y > screen_height - snake_size
            ):
                game_over = True
                pygame.mixer.music.load("sound/gameover2.mp3")
                pygame.mixer.music.play()

            plot_snake(game_window, white, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()