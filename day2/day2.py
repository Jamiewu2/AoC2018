from collections import Counter
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
 
