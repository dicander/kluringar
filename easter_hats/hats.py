import itertools

N_PLAYERS = 5
def bit_distance(first, second):
    difference = 0
    for index, value in enumerate(first):
        if second[index] != value:
            difference+=1
    return difference

def smallest_bit_distance(candidate, targets):
    lowest_cost = N_PLAYERS
    for current in targets:
        lowest_cost = min(lowest_cost, bit_distance(candidate, current))
    return lowest_cost

def create_targets():
    targets = []
    for current in itertools.product(range(2),repeat = N_PLAYERS):
        if smallest_bit_distance(current, targets)>=3:
            targets.append(current)
    return targets

def guess(player, fail_these, others):
    if others[:player]+(1,)+others[player:] in fail_these:
        return 0
    elif others[:player]+(0,)+others[player:] in fail_these:
        return 1
    return None

def main():
    correct = 0
    incorrect = 0
    nobody_guessed = 0
    fail_these = create_targets()
    for current in itertools.product(range(2),repeat = N_PLAYERS):
        print(current, sum(current))
        win_condition = False # At least one player is right, no-one is wrong
        for player in range(N_PLAYERS):
            player_guess = guess(player, fail_these, current[:player]+current[player+1:])
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
    print("{0:.4f}% correct answers.".format(100*correct/2**N_PLAYERS))

main()
