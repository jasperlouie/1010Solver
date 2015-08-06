import game, itertools, random

def get_move(board):
	return random.choice(board.get_valid_moves())
