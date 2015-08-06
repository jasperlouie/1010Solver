import game, itertools, time

def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)

def generate_possible_results(board):
	output = [[[],[board]]]
	count = 0
	for i in range(3):
		print("gen {}".format(i))
		print(len(output))
		time.sleep(5)	
		next_gen = []
		for pair in output:
			curr_board = pair[1]
			moves = curr_board.get_valid_moves()
			for move in moves:
				count += 1
				print("simulated {} moves".format(count))
				new_board = curr_board.copy()
				new_board.make_move(move)
				move_list = pair[0][:]
				move_list.append(move)
				next_gen.append([move_list,new_board])
		output = next_gen
	return output

def get_num_free_spaces(board):
	count = 0
	for x in range(10):
		for y in range(10):
			if not board.matrix[x][y]:
				count += 1
	return count

def score_board(board):
	return get_num_free_spaces(board)

move_queue = []
def refresh_move_queue(board):
	possible_results = generate_possible_results(board)
	for pair in possible_results:
		pair.append(score_board(pair[1]))
	sorted_possible_results = sorted(possible_results, key=lambda x: x[2], reverse=True)
	return sorted_possible_results[0]

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
