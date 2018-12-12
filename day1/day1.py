import itertools

# part 1
with open("input.txt", 'r') as file:
    total = sum([int(line.strip()) for line in file])
    print(total)

# part 2
with open("input.txt", 'r') as file:
    
    frequency_list = [int(line.strip()) for line in file]
    current_count = 0
    seen = set()
    for element in itertools.cycle(frequency_list):
        current_count += element
        if current_count in seen:
            print(current_count)
            break
        else:
            seen.add(current_count)

