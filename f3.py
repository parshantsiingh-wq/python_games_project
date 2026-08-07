import pygame
x=pygame.init()
print(x)

# creating window
game_window= pygame.display.set_mode((1000,500))
pygame.display.set_caption("snake water gun")

# game specific variable
exit_game = False
game_over = False

# creating a game loop
while not exit_game:
    for event in pygame.event.get():
        print(event)

pygame.quit()
quit()

