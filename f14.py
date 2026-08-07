import pygame
import random

pygame.init()

screen_width = 1200
screen_height = 600

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 55)



# Function
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, (x, y))


def plot_snake(game_window, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])

    if snk_list:
        head_x, head_y = snk_list[-1]
        pygame.draw.rect(game_window, (0, 100, 0), [head_x, head_y, snake_size, snake_size])

# Game Loop
def game_loop():

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
        hiscore=f.read()


    food_x = random.randint(20, screen_width - 20)
    food_y = random.randint(20, screen_height - 20)

    while not exit_game:

        if game_over:

            with open("f1.txt", "w") as f:
                f.write(str(hiscore))
            game_window.fill(white)
            text_screen("Game Over! Press Enter to Continue", red, 180, 250)

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

            snake_x += velocity_x
            snake_y += velocity_y

            # Food Collision
            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 10


                food_x = random.randint(20, screen_width - 20)
                food_y = random.randint(20, screen_height - 20)

                if score>int(hiscore):
                    hiscore=score

                snk_length += 5

            game_window.fill(white)
            text_screen("Score :  " + str(score) , red, 5, 5)
            text_screen( "hiscore : " + str(hiscore), (255,255,0), 930, 5)

            pygame.draw.rect(game_window, red,
                             [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)


            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            # Snake Collision
            if head in snk_list[:-1]:
                game_over = True

            # Wall Collision
            if (snake_x < 0 or
                snake_x > screen_width - snake_size or
                snake_y < 0 or
                snake_y > screen_height - snake_size):
                game_over = True

            plot_snake(game_window, black, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


game_loop()