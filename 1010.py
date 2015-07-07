class Board:
    """A 10 x 10 list of 0's and 1's
    0 means a space is clear, 1 means it's occupied
    Represents a gamestate of the 10 x 10 board"""
    EMPTY_BOARD = [[0] * 10] * 10
    def __init__(self, matrix = EMPTY_BOARD):
        self.matrix = matrix

class Piece:
    """A list of 2D tuples that contain the coordinates of the blocks in a piece,
    in respect to the top left most block in a piece. Must contain (0,0)"""
    def __init__(self, blocks = [(0,0)]):
        self.blocks = blocks
