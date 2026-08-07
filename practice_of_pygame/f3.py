# file showing a circle moving on screen
import pygame
pygame.init()
screen= pygame.display.set_mode((900, 700))
pygame.display.set_caption("hey parshant ")
clock=pygame.time.Clock()
running= True
dt=0

player_pos=pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
while running:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill("purple")
    pygame.draw.circle(screen, "grey", player_pos,40)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y-=4.8
    if keys[pygame.K_s]:
        player_pos.y+=4.8
    if keys[pygame.K_a]:
        player_pos.x-=4.8
    if keys[pygame.K_d]:
        player_pos.x+=4.8
    pygame.display.update()   # pygame.display.flip()
    clock.tick(60)
pygame.quit()
quit