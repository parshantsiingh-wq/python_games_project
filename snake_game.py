



# NOTE: Replace this file with your original if needed.
# Changes:
# - Background music restarts after ENTER.
# - Food uses Sound() effect.
# - Game over uses Sound() effect.

import pygame
import random
import os

pygame.init()
pygame.mixer.init()

screen_width = 1200
screen_height = 600

bg_image = pygame.image.load("sound/background_img.jpg")
bg_image = pygame.transform.scale(bg_image, (screen_width, screen_height))

eat_sound = pygame.mixer.Sound("sound/gameover1.mp3")
gameover_sound = pygame.mixer.Sound("C:/Users/parsh/PycharmProjects/py_game_module/sound/game_over_sound .wav")

white=(255,255,255); red=(255,0,0); black=(0,0,0)
game_window=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("My First Game")
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)

def text_screen(text,color,x,y):
    game_window.blit(font.render(text,True,color),(x,y))

def plot_snake(win,color,snk,size):
    for x,y in snk:
        pygame.draw.rect(win,color,[x,y,size,size])
    if snk:
        head_x, head_y = snk[-1]
        pygame.draw.rect(game_window, (0,200,255), [head_x, head_y, size, size])

def welcome():
    while True:
        game_window.fill((50,205,50))
        text_screen("Welcome to Snake Game",black,340,220)
        text_screen("Press SPACE to Play",black,380,280)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                 over=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                pygame.mixer.music.load("sound/gamemusic1.mp3")
                pygame.mixer.music.play(-1)
                game_loop()

def game_loop():
    if not os.path.exists("f1.txt"):
        open("f1.txt","w").write("0")
    hiscore=int(open("f1.txt").read())
    score=0
    snake_x,snake_y=45,55
    vx=vy=0
    speed=5
    size=15
    food_x=random.randint(20,1180)
    food_y=random.randint(20,580)
    snk=[]; ln=1
    over=False
    while True:
        if over:
            open("f1.txt","w").write(str(hiscore))
            game_window.fill(white)
            text_screen("Game Over! Press ENTER",red,340,250)
            pygame.display.update()
            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    pygame.quit(); raise SystemExit
                if e.type==pygame.KEYDOWN and e.key==pygame.K_RETURN:
                    pygame.mixer.music.load("sound/gamemusic1.mp3")
                    pygame.mixer.music.play(-1)
                    return game_loop()
            clock.tick(30)
            continue
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                exit_game=True
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_RIGHT:vx,vy=speed,0
                if e.key==pygame.K_LEFT:vx,vy=-speed,0
                if e.key==pygame.K_UP:vx,vy=0,-speed
                if e.key==pygame.K_DOWN:vx,vy=0,speed
                if e.key == pygame.K_q:score += 50
        snake_x+=vx; snake_y+=vy
        if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
            eat_sound.play()
            score+=10
            ln+=5
            if score>hiscore: hiscore=score
            food_x=random.randint(20,1180); food_y=random.randint(20,580)
        game_window.blit(bg_image,(0,0))
        text_screen("Score :  " + str(score), white, 5, 5)
        text_screen("hiscore : " + str(hiscore), (255, 255, 0), 930, 5)
        pygame.draw.rect(game_window,red,[food_x,food_y,size,size])
        head=[snake_x,snake_y]; snk.append(head)
        if len(snk)>ln: del snk[0]
        if head in snk[:-1] or snake_x<0 or snake_x>1185 or snake_y<0 or snake_y>585:
            over=True
            pygame.mixer.music.stop()
            gameover_sound.play()
        plot_snake(game_window,white,snk,size)
        pygame.display.update()
        clock.tick(40)

welcome()