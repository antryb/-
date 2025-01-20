import pygame
from copy import deepcopy
from random import choise, randrange

FPS = 120
W, H = 10, 16
TILE = 40
WIDTH, HEIGHT = W*TILE, H*TILE
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # установка размера
clock = pygame.time.Clock()
pygame.display.update()
pygame.init()
game_screen = pygame.display.set_mode((WIDTH, HEIGHT))

grid = [pygame.Rect(x*TILE, y*TILE,TILE,TILE)for x in range(W) for y in range(H)]

figures_pos = [[(-1,0),(-2,0),(0,0),(1,0)],
                [(0,-1),(-1,-1),(-1,0),(0,0)],
                [(-1,0),(-1,1),(0,0),(0,-1)],
                [(0,0),(-1,0),(0,1),(-1,-1)],
                [(0,0),(0,-1),(0,1),(-1,-1)],
                [(0,0),(0,-1),(0,1),(1,-1)],
                [(0,0),(0,-1),(0,1),(-1,0)]]

figures =[[pygame.Rect(x+W//2,y+1,1,1)for x, y in fig_pos]for fig_pos in figures_pos]
figure_rect = pygame.Rect(0,0,TILE-4,TILE-4)
figure = deepcopy(choise(figures)) # текушая фигура

count, speed, limit = 0, 60, 2000

field = [[0 for i in range(W)] for j in range (H)]

def check_borders():  #  проверка границ
    return (figure[i].x < 0 or (figure[i].x > W -1)) or (figure[i].y > H-1 or 
                                                         field [figure[i].y][figure[i].x])
while True:
    dx = 0
    screen.fill((0,0,0))
    clock.tick(FPS)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            if event.key == pygame.K_RIGHT:
                dx = 1
            if event.key == pg.K_DOWN:
            limit = 100

    figure_old = deepcopy(figure)   
    for i in range(4):  #   move to x
        figure[i].x += dx
        if check_borders():
            figure = deepcopy(figure_old)
            break

    count+=speed
    if count>limit:
        count=0
        figure_old=deepcopy(figure)
        for i in range(4):
            figure[i].y+=1
            if check_borders():
                for j in range(4):
                    field[figure_old[j].y][figure_old[j].x] = pg.color('White')
                    figure = deepcopy(choise(figures))
                    limit = 2000
                    break

    center = figure[0]
    figure_old = deepcopy(figure)
    if rotate:
        for i in range(4):
            x=figure[i].y - center

    [pygame.draw.rect(screen,(50,50,50),i,1)for i in grid]

    for i in range(4):
        figure_rect.x = figure[i].x*TILE
        figure_rect.y = figure[i].y*TILE
        pygame.draw.rect(screen,(255,255,255),figure_rect)

    for y, raw in enumerate(field):
        for x, col in enumerate(raw):
            if col:
                figure_rect.x, figure_rect.y = x * TILE, y * TILE
                pygame.draw.rect(game_screen, col, figure_rect)

        pygame.display.update()
        clock.tick(FPS)

    pygame.display.update()