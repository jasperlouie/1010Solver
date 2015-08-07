import game, random, greedy_alg
def get_move(board):
	# if move_queue == []:
	# 	refresh_move_queue(board)
	max_score = -1
	score_move_dict = {}
	for move in board.get_valid_moves():
		new_board = board.copy()
		pair = new_board.make_move(move)
		# print(pair)
		score_move_dict[score_board(new_board)] = move
	max_key = max(score_move_dict.keys()) 
	return score_move_dict[max_key]

def score_board(board):
	# if can_place_all_pieces(board):
	# 	return get_num_free_lines(board)*100+get_num_free_spaces(board)+200
	# return get_num_free_lines(board)*100+get_num_free_spaces(board)
	return 100000 - (greedy_alg.get_num_free_lines(board)*40 + greedy_alg.can_place_all_pieces(board)*100)
	