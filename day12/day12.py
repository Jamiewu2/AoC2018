# part 1
from typing import Dict


class Pots:
    def __init__(self, state: str, rules: Dict[str, str]):
        self.state = state
        self.rules = rules
        self.zero_offset = 0

    def sum_of_pots_metric(self) -> int:
        pots_metric = 0
        for i, char in enumerate(self.state):
            actual_location = i - self.zero_offset
            if char == '#':
                pots_metric += actual_location

        return pots_metric

    def pprint(self):
        print(self.state)
        print(self.rules)
        print(self.zero_offset)

    def apply_iteration(self):
        padded_state = f"....{self.state}...."  # add some padding. This assumes that `.....` -> `.` always
        new_state = list(padded_state)
        for i, char in enumerate(padded_state[2:-2], 2):
            rule_key = padded_state[i-2:i+3]
            new_pot_state = self.rules[rule_key]
            new_state[i] = self.rules[rule_key]

        new_state_str = ''.join(new_state)
        self.state = new_state_str

        self.zero_offset += 4  # shift by 4 every time because of the padding



def parse_file(filename: str) -> Pots:
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = list(map(lambda line: line.strip(), lines))
        lines = list(filter(None, lines))

        #first line is initial state
        initial_state = lines[0].split()[-1].strip()  # remove label
        rules = lines[1:]
        rules_dict = dict(((x[:5], x[-1]) for x in rules))
        return Pots(initial_state, rules_dict)

# part 1

#pots_start_state = parse_file('input.txt')
#pots_start_state.pprint()
#for i in range(20):
#    pots_start_state.apply_iteration()
#print(pots_start_state.sum_of_pots_metric())


# part 2

#obviously, running 50 billion iterations is not feasible, so there must be some pattern
#the question reminds me of Conway's game of life, so it should probably stabilize into some repeatable pattern
#so lets see the diff between iterations


pots_start_state = parse_file('input.txt')
last_metric = 0
for i in range(1, 1000):
    pots_start_state.apply_iteration()
    new_metric = pots_start_state.sum_of_pots_metric()
    diff = new_metric - last_metric
    last_metric = new_metric
    print(f"iteration {i} | metric={new_metric} | diff={diff}")

# this outputs
"""
...
iteration 98 | metric=4108 | diff=16
iteration 99 | metric=4146 | diff=38
iteration 100 | metric=4184 | diff=38
iteration 101 | metric=4222 | diff=38
iteration 102 | metric=4260 | diff=38
iteration 103 | metric=4298 | diff=38
iteration 104 | metric=4336 | diff=38
iteration 105 | metric=4374 | diff=38
iteration 106 | metric=4412 | diff=38
iteration 107 | metric=4450 | diff=38
iteration 108 | metric=4488 | diff=38
iteration 109 | metric=4526 | diff=38
iteration 110 | metric=4564 | diff=38
iteration 111 | metric=4602 | diff=38
iteration 112 | metric=4640 | diff=38
iteration 113 | metric=4678 | diff=38
iteration 114 | metric=4716 | diff=38
...
"""

# so, the pattern is to simply add 38 to whatever the last iteration is after iteration 99
print((50000000000 - 100) * 38 + 4184)


