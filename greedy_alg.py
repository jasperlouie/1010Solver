import game, itertools, time, random, naive_alg

def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)



def get_best_move_seqs(board):
	output = []
	max_score = -1
	curr_gen = []

	for move in board.get_valid_moves():
		curr_gen.append([move])
	# count = 0
	for i in range(2):
		# print("gen {}".format(i))
		# print(len(output))
		# time.sleep(5)	
		next_gen = []
		for move_seq in curr_gen:
			pre_board = board.copy()
			for move in move_seq:
				pre_board.make_move(move)
			new_moves = pre_board.get_valid_moves()
			for new_move in new_moves:
				# count += 1
				# print("simulated {} moves".format(count))
				if i == 1:
					curr_board = pre_board.copy()
					# print "THIS IS THE BOARD I SEE"
					# print curr_board
					curr_board.make_move(new_move)
					
					score = score_board(curr_board)
					if score > max_score:
						# print score
						curr_move_seq = list(move_seq)
						curr_move_seq.append(new_move)
						# print curr_move_seq
						output = [curr_move_seq]
						max_score = score
					elif score == max_score:
						curr_move_seq = list(move_seq)
						curr_move_seq.append(new_move)
						# print curr_move_seq
						output.append(curr_move_seq)
					# print output
				else:
					curr_move_seq = list(move_seq)
					curr_move_seq.append(new_move)
					# print curr_move_seq
					next_gen.append(curr_move_seq)
		curr_gen = next_gen
	return output

def get_num_free_spaces(board):
	count = 0
	for x in range(10):
		for y in range(10):
			if board.matrix[x][y] == 0:
				count += 1
	return count

def get_num_free_lines(board):
	count = 20
	for x in range(10):
		for y in range(10):
			if board.matrix[x][y] == 1:
				count -= 1
				break
	for y in range(10):
		for x in range(10):
			if board.matrix[x][y] == 1:
				count -= 1
				break
	return count

def can_place_all_pieces(board):
	biggest_pieces = [game.piece_dict['e'],game.piece_dict['i'],game.piece_dict['s']]
	score = 0
	for piece in biggest_pieces:
		board.current_pieces = [piece]
		if board.has_valid_moves():
			score += 150
	return score
def squared_continuous_spaces(board):
	score = 0
	count = 0
	for x in range(10):
		for y in range(10):
			if board.matrix[x][y] == 0:
				count += 1
			else:
				score += count**2
				count = 0
	return score

def score_board(board):
	# if can_place_all_pieces(board):
	# 	return get_num_free_lines(board)*100+get_num_free_spaces(board)+200
	# return get_num_free_lines(board)*100+get_num_free_spaces(board)
	return squared_continuous_spaces(board) + can_place_all_pieces(board)


move_queue = []
def refresh_move_queue(board):
	global move_queue
	best_moves = get_best_move_seqs(board)
	# print("Best Moves: ")
	# print(best_moves)
	# print best_moves
	# move_queue = random.choice(best_moves)
	if best_moves != []:
		move_queue = best_moves[0]



def get_move(board):
	global move_queue
	if move_queue == []:
		refresh_move_queue(board)
	if move_queue == []:
		move_queue = [naive_alg.get_move(board)]
	# print move_queue
	move = move_queue.pop(0)
	# print move
	return move

# def get_move_misere(board):
