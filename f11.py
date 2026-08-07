import pygame
import random

pygame.init()
screen_width = 1200
screen_height = 600

# colors

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("my first game")
pygame.display.update()

# game specific variable


# pycharm game controler timer
clock=pygame.time.Clock()

font = pygame.font.SysFont(None,55)

# function

def text_screen(text, color, x,y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text,(x,y))


def plot_snake(game_window, color, snk_list, snake_size):
    for x,y in snk_list:
      pygame.draw.rect(game_window, black, [x,y, snake_size, snake_size])
    if snk_list:
     head_x, head_y = snk_list[-1]
     pygame.draw.rect(game_window, (0, 100, 0), [head_x, head_y, snake_size, snake_size])

# game loop
def game_loop():
    # variable
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
    food_x = random.randint(20, screen_width // 2)
    food_y = random.randint(20, screen_height // 2)

    while not exit_game:
        if game_over:
            game_window.fill(white)
            text_screen("Game over! press enter to continue", red, 100,300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=+init_velocity
                        velocity_y = 0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y = 0
                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x = 0
                    if event.key==pygame.K_DOWN:
                        velocity_y=+init_velocity
                        velocity_x = 0

            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y

            if abs(snake_x - food_x)<6 and (snake_y - food_y)<6:
                score+=1
                print("score is : ", score )
                food_x = random.randint(20, screen_width // 2)
                food_y = random.randint(20, screen_height // 2)
                snk_length+=5

            game_window.fill(white)
            text_screen("score is: " + str(score*10) , red,5,5)
            pygame.draw.rect(game_window, red, (food_x, food_y, snake_size, snake_size))

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
                

            if head in snk_list[:-1]:
                game_over=True


            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True

            # pygame.draw.rect(game_window,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(game_window,black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
game_loop()