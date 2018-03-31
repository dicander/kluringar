import itertools

def index_sum(others):
	answer = 0
	for index, current in enumerate(others):
		if current == 1:
			answer += index
	return answer

def guess(player, others):
#print("player", player, "guessing on", others)
	count = sum(others)
	if count == 0:
		return 1
	if count==2:
		return 1
	if count==4:
		return 0
	if count==6:
		return 0
	return None
	


def main():
	correct = 0
	incorrect = 0
	nobody_guessed = 0
	for current in itertools.product(range(2),repeat = 7):
		print(current, sum(current))
		win_condition = False # At least one player is right, no-one is wrong
		for player in range(7):
			player_guess = guess(player, current[:player]+current[player+1:])
			if player_guess != None:
				if player_guess == current[player]:
					print("player {} was right".format(player))
					win_condition = True
				else:
					print("player {} was wrong".format(player))
					incorrect += 1
					break
		else:
			if win_condition:
		 		correct += 1
			else:
				nobody_guessed += 1
				print("unfortunately, nobody guessed!")
	print("correct answers:", correct)
	print("incorrect answers:", incorrect)
	print("{0:.2f}% correct answers.".format(100*correct/128))
main()
