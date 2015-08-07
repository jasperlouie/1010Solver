import game, random
def get_move(board):
	# if move_queue == []:
	# 	refresh_move_queue(board)
	max_score = -1
	score_move_dict = {}
	for move in board.get_valid_moves():
		new_board = board.copy()
		pair = new_board.make_move(move)
		# print(pair)
		score_move_dict[len(pair[0])+len(pair[1])] = move
	max_key = max(score_move_dict.keys()) 
	return score_move_dict[max_key]