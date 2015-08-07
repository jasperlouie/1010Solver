# Starting game loop
############################################################################
import human_input, game, random_strat, greedy_alg, naive_alg
solver_dict = {"human":human_input, "random":random_strat, "greedy":greedy_alg, "naive":naive_alg}
solver = input("Please select a solver from the following by typing its name\n{}\n".format(solver_dict.keys()))
if solver in solver_dict:
	score = game.play(solver_dict[solver].get_move)
print("Game Over! You lasted {} moves and cleared {} lines!".format(score[0],score[1]))