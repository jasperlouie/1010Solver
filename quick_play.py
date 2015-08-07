# Starting game loop
############################################################################
import human_input, game, random_strat, greedy_alg, naive_alg
# solver_dict = {"human":human_input, "random":random_strat, "greedy":greedy_alg, "naive":naive_alg}
# solver = input("Please select a solver from the following by typing its name\n{}\n".format(solver_dict.keys()))
# if solver in solver_dict:
num_games = 200
top_score = [-1,-1]
running_total = [0.0,0.0]
for x in range(num_games):
	score = game.play(naive_alg.get_move,verbose=False)
	if score[0] > top_score[0]:
		top_score = score
	running_total[0] += score[0]
	running_total[1] += score[1]
	print("Game {}: {} pieces placed, {} lines cleared".format(x,score[0],score[1]))

print("\n\nOver the course of {} games, avg pieces placed: {} avg lines cleared: {}".format(num_games,
	running_total[0]/num_games,running_total[1]/num_games))
print("Your top score: {} pieces placed, {} lines cleared".format(top_score[0], top_score[1]))