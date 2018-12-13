from collections import Counter
from itertools import combinations
# part 1

# well apparently, a regex for searching for any character exactly twice
# is much more difficult than I thought it would be
# these don't work
# regex2 = r"([a-zA-Z])[^\1]*\1[^\1]*$"
# regex3 = r"([a-zA-Z]).*\1.*\1"

with open('input.txt', 'r') as file:

    number_of_exactly_2 = 0
    number_of_exactly_3 = 0
    
    for line in file:
        line = line.strip()
        count = Counter(line)
        if 2 in count.values():
            number_of_exactly_2 += 1
        if 3 in count.values():
            number_of_exactly_3 += 1
                
    print(number_of_exactly_2)
    print(number_of_exactly_3)
    print(number_of_exactly_2 * number_of_exactly_3)
 
# part 2

def is_one_different(first: str, second: str) -> bool:
	if len(first) != len(second): # assuming same length strings
		raise Exception()

	if first[0] == second[0]:
		return check_if_one_different(first[1:], second[1:])
	else:
		return first[1:] == second[1:]


with open('input.txt', 'r') as file:
	lines = file.readlines()
	lines = map(lambda x: x.strip(), lines)
	for (first, second) in combinations(lines, 2):
		if is_one_different(first, second):
			print(first, second)
			same_chars = ''.join([f for (f,s) in zip(first,second) if f == s ])
			print(same_chars)
