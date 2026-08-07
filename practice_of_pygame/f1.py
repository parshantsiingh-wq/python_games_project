import pygame
pygame.init()
screen= pygame.display.set_mode((900, 700))
pygame.display.set_caption("hey parshant ")
clock=pygame.time.Clock()
running= True
while running:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill("purple")
    pygame.display.update()   # pygame.display.flip()
    clock.tick(60)
pygame.quit()
quit