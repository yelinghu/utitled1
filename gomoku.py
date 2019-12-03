from enum import Enum

import boardstate
from boardstate import *

class Gomoku(object):

    def __init__(self):
        #create a map
        self.__chessMap = [[BoardState.EMPTY for j in range(N)] for i in range(N)]
        # currenti, current j, current state state this move's location and color
        self.__currentI = -1
        self.__currentJ = -1
        self.__currentState = BoardState.EMPTY

        def get_chessMap(self):
            return self.__chessMap

        def get_chessboard_state(self, i, j):
            return self.__chessMap[i][j]

        def set_chessboard_state(self,  i,  j,   state):

            self.__chessMap[i][j] = state
            self.__currentI = i
            self.__currentJ = j
            self.__currentState = state

        def count_on_direction(self, i, j, xdirection, ydirection, color):
            count = 0
            for step in range(1, 5):  # check four more point
                if xdirection != 0 and (j + xdirection * step < 0 or j + xdirection * step >= N):
                    break # over board
                if ydirection != 0 and (i + ydirection * step < 0 or i + ydirection * step >= N):
                    break
                if self.__chessMap[i + ydirection * step][j + xdirection * step] == color:
                    count += 1
                else:
                    break
            return count

        def have_five(self, i, j, color):
            # four direction
            directions = [[(-1, 0), (1, 0)],
                          [(0, -1), (0, 1)],
                          [(-1, 1), (1, -1)],
                          [(-1, -1), (1, 1)]]

            for axis in directions:
                axis_count = 1
                for (xdirection, ydirection) in axis:
                    axis_count += self.count_on_direction(i, j, xdirection, ydirection, color)
                    if axis_count >= 5:
                        return True

            return False

        def get_chess_result(self):
            if self.have_five(self.__currentI, self.__currentJ, self.__currentState):
                return self.__currentState
            else:
                return BoardState.EMPTY