import pygame
from pygame.locals import *
from sys import exit

import boardstate
from boardstate import *
from gomoku import Gomoku
from render import GameRender
#from gomoku_ai import *

if __name__ == '_main_':
    gomoku= Gomoku()
    render = GameRender(gomoku)
    #ai =  GomokuAI(gomoku, board.BLACK, 2)
    #ai2 = GomokuAI(gomoku, board.WHITE, 1)

    result= BoardState.EMPTY

    enable_ai = False
    """
    enable_ai = False
    ai.first_step()
    result = gomoku.get_chess_result()
    render.change_state()
    """
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exec()

            if event.type == MOUSEBUTTONDOWN:
                if render.one_step():
                    result= gomoku.get_chess_result()
                else:
                    continue

                if result != BoardState.EMPTY:
                    break
                if enable_ai:
                    # ai.one_step()
                    result=gomoku.get_chess_result()

                else:
                    render.change_state()

    render.draw_chess()
    render.draw_mouse()

    if result != ChessboardState.EMPTY:
        render.draw_result(result)

    pygame.display.update()




