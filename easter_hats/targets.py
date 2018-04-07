import itertools

def bit_distance(first, second):
    difference = 0
    for index, value in enumerate(first):
        if second[index] != value:
            difference+=1
    return difference

def smallest_bit_distance(candidate, targets):
    lowest_cost = 7
    for current in targets:
        lowest_cost = min(lowest_cost, bit_distance(candidate, current))
    return lowest_cost

def create_targets():
    targets = []
    for current in itertools.product(range(2),repeat = 7):
        if smallest_bit_distance(current, targets)>=3:
            targets.append(current)
    return targets

def test():
    targets = create_targets()
    print(len(targets), "targets found")
    print(targets)


