# Starting game loop
############################################################################
import human_input, game, random_strat, greedy_alg, naive_alg, time, datetime
solver_dict = {"human":human_input, "random":random_strat, "greedy":greedy_alg, "naive":naive_alg, "replay":None}
solver = input("Please select a solver from the following by typing its name\n{}\n".format(solver_dict.keys()))
if solver == "replay":
	score = game.replay(input("enter replay string:\n"))
elif solver in solver_dict:
	start = time.clock()
	score = game.play(solver_dict[solver].get_move)
	end = time.clock()
	elapsed = end - start
	# game.Result(score[2], start, elapsed, score[3], [solver])
print("Game Over! You score {} points, lasted {} moves and cleared {} lines!\nThe game lasted {}".format(score[2],score[0],score[1], str(datetime.timedelta(seconds=elapsed))))