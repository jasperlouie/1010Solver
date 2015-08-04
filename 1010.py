import random

class Board:
    """A 10 x 10 list of 0's and 1's, 0 means a space is clear, 1 means it's occupied. Represents a gamestate of the 10 x 10 board
    On this board, the coordinates system starts with (0,0) being the top left corner, and the first coordinate being the x, and the second being the y."""
    EMPTY_BOARD = [[0] * 10] * 10

    """Constructs a Board. Default is empty"""
    def __init__(self, matrix = EMPTY_BOARD):
        self.matrix = matrix

    """Returns True if you can place Piece p at the Location loc"""
    def is_valid_move(self, p, loc):
        for block in p.blocks:
            currX, currY = block[0] + loc[0], block[1] + loc[1]
            if currX not in range(10) or currY not in range(10) or self.matrix[currX, currY] == 1:
                return False
        return True

    """Returns a list of numbers containing the numbers of the rows that are currently full in the board"""
    def get_full_rows(self):
        output = []
        for y in range(10):
            found0 = False
            for x in range(10):
                output
                if self.matrix[x][y] == 0:
                    found0 = True
                    break
            if not found0:
                output.append(y)
        return output

    """Returns a list of numbers containing the numbers of the columns that are currently full in the board"""
    def get_full_cols(self):
        output = []
        for x in range(10):
            if 0 not in self.matrix[x]:
                output.append(x)
        return output


    """Places a piece p at a space loc (given by a tuple with two coordinates), updates board accordingly"""
    def place_piece(self, p, loc):
        if self.is_valid_move(p , loc):
            # placing piece
            for block in p.blocks:
                self.matrix[block[0] + loc[0]][block[1] + loc[1]] = 1
            # clearing appropriate rows/cols
            full_rows, full_cols = self.get_full_rows(), self.get_full_cols()
            for y in full_rows:
                for x in range(10):
                    self.matrix[x][y] = 0
            for x in full_cols:
                for y in range(10):
                    self.matrix[x][y] = 0
        else:
            raise InvalidMoveException('this is not a valid move')

    def __str__(self):
        
        for y in range(10):
            out = '-' * 21 + '\n'
            out += '|'
            for x in range(10):
                if self.matrix[x][y] == 0:
                    out += ' '
                else:
                    out += 'X'
                out+= '|'
            out += '\n'
        out += '-' * 21
        return out

class Piece:
    """A list of tuples that contain the coordinates of the blocks in a piece,
    in respect to the left most block in the top row of a piece. This block is represented by (0,0)."""
    def __init__(self, blocks = [(0,0)]):
        self.blocks = blocks

    def __str__(self):
        out = ""
        x_offset = 0
        y_offset = 0
        width = 0
        height = 0
        for block in self.blocks:
            width = max(width, block[0]+1)
            height = max(height, block[1]+1)
            x_offset = max(x_offset,-block[0])
            y_offset = max(y_offset,-block[1])
        width += x_offset
        height += y_offset
        for y in range(height):
            for x in range(width):
                if (x-x_offset,y-y_offset) in self.blocks:
                    out += 'X'
                else:
                    out += ' '
            out += '\n'
        return out


    # as an example, a piece that is three blocks horizontally would be [(0,0),(1,0),(2,0)]

# Starting game loop
############################################################################
game_over = False
piece_list = [
Piece(), #singleton
Piece([(0,0),(1,0)]), #2 horizontal
Piece([(0,0),(1,0),(2,0)]), #3 horizontal
Piece([(0,0),(1,0),(2,0),(3,0)]), #4 horizontal
Piece([(0,0),(1,0),(2,0),(3,0),(4,0)]), #5 horizontal
Piece([(0,0),(0,1)]), #2 vertical
Piece([(0,0),(0,1),(0,2)]), #3 vertical
Piece([(0,0),(0,1),(0,2),(0,3)]), #4 vertical
Piece([(0,0),(0,1),(0,2),(0,3),(0,4)]), #5 vertical
Piece([(0,0),(0,1),(1,1)]), #short L
Piece([(0,0),(0,1),(-1,1)]), #short L mirrored
Piece([(0,0),(0,1),(1,0)]), #short L flipped
Piece([(0,0),(1,1),(1,0)]), #short L mirrored flipped
Piece([(0,0),(0,1),(0,2),(1,2),(2,2)]), #Long L
Piece([(0,0),(0,1),(0,2),(-1,2),(-2,2)]), #Long L mirrored
Piece([(0,0),(0,1),(0,2),(1,0),(2,0)]), #short L flipped
Piece([(0,0),(2,1),(2,2),(1,0),(2,0)]), #short L mirrored flipped
Piece([(0,0),(0,1),(1,0),(1,1)]), #2x2
Piece([(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]) #3x3
]

count = 0
current_pieces = []
while not game_over:
    count += 1
    if count > 100:
        break
    print ("Piece Set {}".format(count))
    for num in range(3):
        current_pieces.append(random.choice(piece_list))
    while current_pieces != []:
        print("These are the current pieces")
        for i in range(len(current_pieces)):
            print ("{})".format(i+1))
            print (current_pieces[i])
        
