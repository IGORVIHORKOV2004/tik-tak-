import pygame

def draw_circle(sc, x,y,size):# создание функции для создания кружка
    size=200 # ширина ячейки
    a=  x *    size    +   0.5    *   size # координаты по x
    b=  y *    size    +   0.5 *  size #координаты по y
    pygame.draw.circle(sc,(0,0,255),(a,b),100) # отрисовка кружка

def draw_cross(sc, x,y,size):
    size=200
    a=x*200
    b=y*200
    a1= a+200
    b1=b+200
    pygame.draw.line(sc,(255,0,0,),(a,b),(a1,b1),5)
    pygame.draw.line(sc,(255,0,0,),(a1,b),(a,b1),5)
class Board:
    def __init__(self,W,H,size):
        self.W = W
        self.H=H
        self.size=size
        self .board=[
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        self.move=1

    def click(self,mouse_pos):
     x=mouse_pos[0]//self.size
     y=mouse_pos[1]//self.size
     self.board[y][x]=self.move
     self.move=-self.move
    def render(self,screen):
        pygame.draw.line(screen, (0,0,0), (0, 200), (self.W, 200), 5)
        pygame.draw.line(screen, (0,0,0), (0, 400), (self.W, 400), 5)
        pygame.draw.line(screen, (0,0,0), (200, 0), (200, self.H), 5)
        pygame.draw.line(screen, (0,0,0), (400,0), (400, self.H), 5)
        for y in range(3):
            for x in range(3):
                if self.board[y][x]==1:
                    draw_cross(screen,x,y,self.size)
                elif self.board[y][x]== -1:
                    draw_circle(screen,x,y,self.size)
    def clean_2(self):
        for y in range(3):
            for x in range(3):
                self.board[y][x]=0
                self.move=1
    def is_end(self,board):
            def check_i_col(x,i):
                if x[0][i]==x[1][i]==x[2][i] !=0:
                    return True
                else:
                    return False

            def check_i_line(x,i):
                if x[i][0] == x[i][1]==x[i][2] !=0:
                    return True
                else:
                    return False

            def check_main_daig(x):
                if x[0][0]==x[1][1]==x[2][2] !=0:
                    return  True
                else:
                    return  False
            def check_secondary_daig(x):
                if x[2][0]==x[1][1]==x[0][2] !=0:
                    return True
                else:
                        return   False

            for i in range(3):
                if check_i_col(board,i):
                    return "col",i
                if check_i_line(board,i):
                    return "line", i
                if check_main_daig(board):
                    return "daig",1
                if check_secondary_daig(board):
                      return "diag",2
            return  None

    def check_end(self,screen):
        is_end_info=self.is_end(self.board)
        shift=self.W// 10
        if is_end_info is not None:
            type_end=is_end_info[0]
            number=is_end_info[1]
            if type_end=="col":
                x0,y0=(number + .5) * self.size,shift
                x1,y1=self.size *3 - shift(number + .5)* self.size
            elif type_end=="diag":
                if number == 1:
                    x0, y0 = (number + .5) * self.size, shift
                    x1, y1 = self.size * 3 - shift(number + .5) * self.size
                elif type_end=="diag":
                    if number == 1:
                        x0,y0= shift,shift
                        x1=self.size * 3 - shift
                        y1=self.size * 3 - shift
                    else:
                        x0=self.size * 3 - shift
                        y0= shift
                        x1=shift
                        y1=self.size * 3 - shift

            pygame.draw.line(screen,(255,0,0),(x0,y0),(x1,y1),10)
            pygame.display.update()
            pygame.time.delay(3000)
            return True
        else:
            return  False
