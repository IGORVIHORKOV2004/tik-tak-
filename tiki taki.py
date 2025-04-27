import pygame

from krestiki_ihorkoviki import Board

pygame.init()

height=600
width= 600
board = Board(600,600,200,)
window=pygame.display.set_mode((600,600)) #создание окна размером 300 на 300
FPS=30
clock=pygame.time.Clock()
while True:
    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        board.clean_2()

    if keys[pygame.K_ESCAPE]:
        pygame.guit()
        exit()
        #отрисовка
        board.render(window)

    #проверяем состояние игры
    board.check_end(window)

    '''Конец игровой логики'''
