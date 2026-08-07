import pygame
pygame.init()
screen=pygame.display.set_mode((900,500))
pygame.display.set_caption("movement of object")

player_x=200
player_y= 400
intial=20
size_x=100
size_y=90
fps=60

obj=pygame.time.Clock()
exit=False
while not exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 4.8
    if keys[pygame.K_RIGHT]:
        player_x += 4.8
    screen.fill((145, 186, 135))
    pygame.draw.rect(screen, "white", [player_x, player_y, size_x, size_y])
    pygame.display.update()
    obj.tick(fps)

pygame.quit()
quit