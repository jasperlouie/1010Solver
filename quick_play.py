# Starting game loop
############################################################################
import human_input, game, random_strat, greedy_alg, naive_alg, misere
# solver_dict = {"human":human_input, "random":random_strat, "greedy":greedy_alg, "naive":naive_alg}
# solver = input("Please select a solver from the following by typing its name\n{}\n".format(solver_dict.keys()))
# if solver in solver_dict:
num_games = 100
top_score = [-1,-1,-1]
running_total = [0.0,0.0,0.0]
worst_score = [999,999,999]
for x in range(num_games):
	score = game.play(random_strat.get_move,verbose=False)
	if score[2] > top_score[2]:
		top_score = score
	if score[2] < worst_score[2]:
		worst_score = score
	running_total[0] += score[0]
	running_total[1] += score[1]
	running_total[2] += score[2]
	print("Game {}: {} pieces placed, {} lines cleared, score: {}".format(x,score[0],score[1], score[2]))

print("\n\nOver the course of {} games, avg pieces placed: {} avg lines cleared: {} avg score:{}".format(num_games,
	running_total[0]/num_games,running_total[1]/num_games,running_total[2]/num_games))
print("Your top score: {} pieces placed, {} lines cleared, with a score of {}".format(top_score[0], top_score[1], top_score[2]))
print(top_score[3])
print("Your worst score: {} pieces placed, {} lines cleared, with a score of {}".format(worst_score[0], worst_score[1], worst_score[2]))
print(worst_score[3])