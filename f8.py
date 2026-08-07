import pygame

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
fps=60

# pycharm game controler timer
clock=pygame.time.Clock()

# game loop
while not exit_game:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit_game = True
        # if event.type==pygame.KEYDOWN:
        #     if event.key==pygame.K_RIGHT:
        #         snake_x=snake_x+20
        #     if event.key==pygame.K_LEFT:
        #         snake_x=snake_x-20
        #     if event.key==pygame.K_UP:
        #         snake_y=snake_y-20
        #     if event.key==pygame.K_DOWN:
        #         snake_y=snake_y+20
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake_y -= 4.8
    if keys[pygame.K_DOWN]:
        snake_y += 4.8
    if keys[pygame.K_LEFT]:
        snake_x -= 4.8
    if keys[pygame.K_RIGHT]:
        snake_x += 4.8


    game_window.fill(white)
    pygame.draw.rect(game_window,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()