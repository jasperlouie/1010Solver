import random, time, datetime

class InvalidMoveException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
class Piece:
    """A list of tuples that contain the coordinates of the blocks in a piece,
    in respect to the left most block in the top row of a piece. This block is represented by (0,0)."""
    def __init__(self, blocks, name, char_rep):
        self.blocks = blocks
        self.name = name
        self.char_rep = char_rep
    # as an example, a piece that is three blocks horizontally would be [(0,0),(1,0),(2,0)]

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

class Move:
    def __init__(self, piece, x, y):
        self.piece = piece
        self.x = x
        self.y = y

    def __str__(self):
        return "{} at {},{}".format(self.piece.name,self.x,self.y)

    def __repr__(self):
        return '\n' + str(self)

    def export_as_str(self):
        return chr((10*self.y+self.x)+32)+ self.piece.char_rep

def import_move_as_str(string):
    return Move(piece_dict[string[1]], (ord(string[0])-32)%10, ((ord(string[0])-32)//10))



class Board:
    """A 10 x 10 list of 0's and 1's, 0 means a space is clear, 1 means it's occupied. Represents a gamestate of the 10 x 10 board
    On this board, the coordinates system starts with (0,0) being the top left corner, and the first coordinate being the x, and the second being the y."""
    # EMPTY_BOARD = [[0] * 10 for x in range(10)]
    """Constructs a Board. Default is empty"""
    def __init__(self, matrix = None, current_pieces = [], move_str = ''):
        if matrix == None:
            self.matrix = [[0] * 10 for x in range(10)]
        else:
            self.matrix = matrix
        self.current_pieces = current_pieces[:]
        self.move_str = ''


    def copy(self):
        """Returns a new board identical to self"""
        new_matrix = []
        for col in self.matrix:
            new_matrix.append(col[:])
        return Board(new_matrix, self.current_pieces[:], self.move_str[:])

    """Returns True if you can place Piece p at the Location loc"""
    def is_valid_move(self, move):
        if not move.piece in self.current_pieces:
            return False  
        for block in move.piece.blocks:
            currX, currY = block[0] + move.x, block[1] + move.y
            if currX not in range(10) or currY not in range(10) or self.matrix[currX][currY] == 1:
                return False
        return True

    def get_valid_moves(self):
        out = []
        for piece in self.current_pieces:
            for x in range(10):
                for y in range(10):
                    move = Move(piece, x, y)
                    if self.is_valid_move(move):
                        out.append(move)
        return out

    def has_valid_moves(self):
        for piece in self.current_pieces:
            for x in range(10):
                for y in range(10):
                    move = Move(piece, x, y)
                    if self.is_valid_move(move):
                        return True
        return False


    """Returns a list of numbers containing the numbers of the rows that are currently full in the board"""
    def get_full_rows(self):
        output = []
        for y in range(10):
            found0 = False
            for x in range(10):
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


    """Places a piece p at a space loc (given by a tuple with two coordinates), updates board accordingly
        Returns a tuple of two lists that contains rows and cols cleared respectively"""
    def make_move(self, move):
        if self.is_valid_move(move):
            move_str = move.export_as_str()
            # placing piece
            for block in move.piece.blocks:
                self.matrix[block[0] + move.x][block[1] + move.y] = 1
            # clearing appropriate rows/cols
            full_rows, full_cols = self.get_full_rows(), self.get_full_cols()
            for y in full_rows:
                move_str += "{}y".format(y)
                for x in range(10):
                    self.matrix[x][y] = 0
            for x in full_cols:
                move_str += "{}x".format(x)
                for y in range(10):
                    self.matrix[x][y] = 0
            self.current_pieces.remove(move.piece)
            self.move_str += move_str 
            return full_rows, full_cols
        else:
            print("Here is a string representing the current board:")
            print(self.export_as_str())
            raise InvalidMoveException('{} is not a valid move'.format(move))

    """Places a piece p at a space loc (given by a tuple with two coordinates), updates board accordingly
        Returns a tuple of two lists that contains rows and cols cleared respectively"""
    def force_move(self, move):
        # placing piece
        move_str = move.export_as_str()
        for block in move.piece.blocks:
            self.matrix[block[0] + move.x][block[1] + move.y] = 1
        # clearing appropriate rows/cols
        full_rows, full_cols = self.get_full_rows(), self.get_full_cols()
        for y in full_rows:
            move_str += "{}y".format(y)
            for x in range(10):
                self.matrix[x][y] = 0
        for x in full_cols:
            move_str += "{}x".format(x)
            for y in range(10):
                self.matrix[x][y] = 0
        # self.current_pieces.remove(move.piece)
        self.move_str += move_str
        return full_rows, full_cols

            

    def refresh_pieces(self):
        for num in range(3):
            self.current_pieces.append(random.choice(piece_list))

    def export_as_str(self):
        out = ''
        for x in range(10):
            for y in range(10):
                if self.matrix[x][y] == 1:
                    out += '1'
                else:
                    out += '0'
        for piece in self.current_pieces:
            out += piece.char_rep
        return out

    def import_as_str(self, input_str):
        for x in range(10):
            for y in range(10):
                self.matrix[x][y] = int(input_str[x*10+y])
        for char in input_str[100:]:
            self.current_pieces.append(piece_dict[char])

    def undo_move(self):
        "undoes the last move based on the board's move_str"
        index = len(self.move_str) -1
        # print "BEFORE"
        # print self.move_str
        last_char = self.move_str[index]
        while last_char == 'x' or last_char == 'y':
            if  last_char == 'x':
                for y in range(10):
                    self.matrix[int(self.move_str[index-1])][y] = 1
            elif last_char == 'y':
                for x in range(10):
                    self.matrix[x][int(self.move_str[index-1])] = 1
            index -= 2
            last_char = self.move_str[index]
        move = import_move_as_str(self.move_str[index - 1:index + 1])                            
        for block in move.piece.blocks:
            self.matrix[block[0] + move.x][block[1] + move.y] = 0
        self.current_pieces.append(move.piece)
        self.move_str = self.move_str[:index - 1]
        # print "AFTER"
        # print self.move_str

    # def import_move_str(self, move_str):
    #     while x < 
    #     curr_pair = move_str

    def __str__(self):
        out = "  "
        for i in range(10):
            out += " {}  ".format(i)
        out += '\n'
        for y in range(10):
            out += ' '+'-' * 41 + '\n'
            out += '{}| '.format(y)
            for x in range(10):
                if self.matrix[x][y] == 0:
                    out += ' '
                else:
                    out += 'X'
                out+= ' | '
            out += '\n'
        out += ' '+'-' * 41
        out += "\nPieces:"
        for i in range(len(self.current_pieces)):
            out += "\n{})\n".format(i+1)
            out += str(self.current_pieces[i])
        return out




# All possible pieces
piece_list = [
Piece([(0,0)],'single', 'a'), #singleton
Piece([(0,0),(1,0)],'2 horizontal', 'b'), #2 horizontal
Piece([(0,0),(1,0),(2,0)],'3 horizontal', 'c'), #
Piece([(0,0),(1,0),(2,0),(3,0)],'4 horizontal', 'd'), #
Piece([(0,0),(1,0),(2,0),(3,0),(4,0)], '5 horizontal', 'e'), #5 horizontal
Piece([(0,0),(0,1)], '2 vertical', 'f'), #2 vertical
Piece([(0,0),(0,1),(0,2)], '3 vertical', 'g'), #3 vertical
Piece([(0,0),(0,1),(0,2),(0,3)], '4 vertical', 'h'), #4 vertical
Piece([(0,0),(0,1),(0,2),(0,3),(0,4)], '5 vertical', 'i'), #5 vertical
Piece([(0,0),(0,1),(1,1)], 'short L', 'j'), #short L
Piece([(0,0),(0,1),(-1,1)], 'short L mirrored', 'k'), #short L mirrored
Piece([(0,0),(0,1),(1,0)], 'short L flipped', 'l'), #short L flipped
Piece([(0,0),(1,1),(1,0)], 'short L mirrored flipped', 'm'), #short L mirrored flipped
Piece([(0,0),(0,1),(0,2),(1,2),(2,2)], 'Long L', 'n'), #Long L
Piece([(0,0),(0,1),(0,2),(-1,2),(-2,2)], 'Long L mirrored', 'o'), #Long L mirrored
Piece([(0,0),(0,1),(0,2),(1,0),(2,0)], 'Long L flipped', 'p'), #short L flipped
Piece([(0,0),(2,1),(2,2),(1,0),(2,0)], 'Long L mirrored flipped', 'q'), #short L mirrored flipped
Piece([(0,0),(0,1),(1,0),(1,1)], '2x2', 'r'), #2x2
Piece([(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)], '3x3', 's') #3x3
]
import string
piece_dict = dict(zip(string.ascii_lowercase, piece_list))



class Result:
    """Class that defines result of a run, and includes the score, the move string, 
    time stamp, and a list of strings that are tags that can be aggregated"""
    def __init__(self, score, timestamp, length, move_str, tags):
        self.score = score
        self.move_str = move_str
        self.tags = tags
        self.timestamp = timestamp
        self.length = length

def play(get_move, verbose = True):
    move_num = 1
    cleared_lines = 0
    score = 0
    board = Board()
    board.refresh_pieces()

    while board.has_valid_moves():

        if verbose:
            print("##########################################")
            print ("Move {}:".format(move_num))
            print ("Score {}:".format(score))
            print ("Here is the current board: \n"+str(board))
            
        if verbose:
            print("------------------------------------------")
        move = get_move(board)
        # try:
        cleared_rows, cleared_cols = board.make_move(move)
        score += len(move.piece.blocks)
        if verbose:
            print("{}placed at {},{}".format(move.piece,move.x,move.y))
            if cleared_cols != []:
                for col in cleared_cols:
                    print("Cleared Column {}!".format(col))
            if cleared_rows != []:
                for row in cleared_rows:
                    print("Cleared Row {}!".format(row))
        cleared_lines += len(cleared_rows) + len(cleared_cols)
        clear_bonus = 0
        for x in range(len(cleared_rows) + len(cleared_cols)):
            clear_bonus += x + 1
        score += clear_bonus * 10
        move_num += 1
        # except InvalidMoveException:
        #     print("That is an invalid move, please make sure you are placing the piece in a valid space")
        # except:
        #     print("Please enter a valid piece number, enter the correct format for a move: piece_num, x, y")
        if board.current_pieces == []:
            board.refresh_pieces()
    if verbose:
        print("##########################################")
        print ("Move {}:".format(move_num))
        print ("Score: {}".format(score))
        print ("Here is the current board: \n"+str(board))
        print("Import this string to see a replay of the game:\n{}".format(board.move_str))
    return move_num, cleared_lines, score, board, board.move_str

def replay(move_string, verbose = True):
    move_string = move_string.strip("\n")
    move_num = 1
    cleared_lines = 0
    score = 0
    board = Board()
    # board.refresh_pieces()
    while move_string != "":

        if verbose:
            print("##########################################")
            print ("Move {}:".format(move_num))
            print ("Score {}:".format(score))
            print ("Here is the current board: \n"+str(board))
            
        if verbose:
            print("------------------------------------------")
        next_move_chars = 'xx'
        while next_move_chars[1] == 'x' or next_move_chars[1] == 'y':
            next_move_chars = move_string[:2]
            move_string = move_string[2:]
        move = import_move_as_str(next_move_chars)
        
        # try:
        cleared_rows, cleared_cols = board.force_move(move)
        score += len(move.piece.blocks)
        if verbose:
            print("{}placed at {},{}".format(move.piece,move.x,move.y))
            if cleared_cols != []:
                for col in cleared_cols:
                    print("Cleared Column {}!".format(col))
            if cleared_rows != []:
                for row in cleared_rows:
                    print("Cleared Row {}!".format(row))
        cleared_lines += len(cleared_rows) + len(cleared_cols)
        clear_bonus = 0
        for x in range(len(cleared_rows) + len(cleared_cols)):
            clear_bonus += x + 1
        score += clear_bonus * 10
        move_num += 1
        # except InvalidMoveException:
        #     print("That is an invalid move, please make sure you are placing the piece in a valid space")
        # except:
        #     print("Please enter a valid piece number, enter the correct format for a move: piece_num, x, y")
        # if board.current_pieces == []:
            # board.refresh_pieces()
    if verbose:
        print("##########################################")
        print ("Move {}:".format(move_num))
        print ("Score: {}".format(score))
        print ("Here is the current board: \n"+str(board))
        print("Import this string to see a replay of the game:\n{}".format(board.move_str))
    return move_num, cleared_lines, score, board, board.move_str



