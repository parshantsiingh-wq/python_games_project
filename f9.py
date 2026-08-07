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
exit_game = False
game_over = False
snake_x=45
snake_y=55
snake_size=15
velocity_x=0
velocity_y=0
init_velocity=5

fps=40
score=0
food_x=random.randint(20, screen_width//2)
food_y=random.randint(20, screen_height//2)


# pycharm game controler timer
clock=pygame.time.Clock()


# game loop
while not exit_game:
    for event in pygame.event.get():
        print(event)
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

        food_x = random.randint(20, screen_width // 2)
        food_y = random.randint(20, screen_height // 2)

    game_window.fill(white)
    pygame.draw.rect(game_window, red, (food_x, food_y, snake_size, snake_size))
    pygame.draw.rect(game_window, (0,255,0),[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()