from game import *

def get_move(board):
    move_input = input("Please input your move: ")
    return convert_str_to_move(move_input, board.current_pieces)

def convert_str_to_move(string, current_pieces):
    move_list = string.replace(' ', '').split(',')
    try:
    	return Move(current_pieces[int(move_list[0])-1], int(move_list[1]), int(move_list[2]))
    except:
        pass
