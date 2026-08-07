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

while not exit_game:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit_game = True

    game_window.fill(white)
    pygame.draw.rect(game_window,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()

pygame.quit()
quit()