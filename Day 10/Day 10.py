import re
from pprint import pprint

test = False

if test:
    filename = "input_test.txt"
else:
    filename = "input.txt"

with open(filename) as f:
    lines = f.read().splitlines()

lines = [j for j in sorted(int(i) for i in lines)]
power_range = (0, max(lines)+3)
lines = [0] + lines + [max(lines)+3]
sum_1 = 0
sum_3 = 0

for i in range(len(lines)-1):
    if lines[i + 1] - lines[i] == 1:
        sum_1 += 1
    elif lines[i + 1] - lines[i] == 3:
        sum_3 += 1

print(f"Part 1: {sum_1 * sum_3}")

memory = [1]

def no_of_paths(n):
    s=0
    for x in range(n-1, -1, -1):
        if lines[n]-lines[x] <= 3:
            s += memory[x]
        else:
            break
    return s

for x in range(1, len(lines)):
    memory.append(no_of_paths(x))

print(f"Part 2: {memory[-1]}")