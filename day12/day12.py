# part 1
from typing import Dict


class Pots:
    def __init__(self, state: str, rules: Dict[str, str]):
        self.state = state
        self.rules = rules
        self.zero_offset = 0

    def sum_of_pots_metric(self):
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
            print(i, char, rule_key, new_pot_state)

        new_state_str = ''.join(new_state)
        print(padded_state)
        print(new_state_str)
        self.state = new_state_str

        self.zero_offset += 4  # shift by 4 every time



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


pots_start_state = parse_file('input.txt')
pots_start_state.pprint()
for i in range(20):
    pots_start_state.apply_iteration()
print(pots_start_state.sum_of_pots_metric())
# pots_start_state.pprint()
