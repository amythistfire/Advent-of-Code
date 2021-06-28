import re
from pprint import pprint

test = False

if test:
    filename = "input_test.txt"
    length = 5
else:
    filename = "input.txt"
    length = 25

with open(filename) as f:
    lines = f.read().splitlines()

num_list = []
answer = 0

lines = [int(i) for i in lines]
for i in range(len(lines)):
    line = lines[i]
    if i >= length:
        success = False
        for high in range(length):
            for low in range(high):
                # print(f"({i-length+j},{i-length+k}) {num_list[j]} + {num_list[k]} = {num_list[k] + num_list[j]} = {line}")
                if num_list[low] + num_list[high] == line:
                    success = True
        if not success:
            solution1 = line
        num_list.pop(0)

    num_list.append(line)

print(f"Part 1: {solution1}")

for i in range(len(lines)):
    for j in range(i-1):
        total = sum(lines[j:i])
        if total == solution1:
            solution2 = min(lines[j:i]) + max(lines[j:i])
            print(lines[j:i])

print(f"Part 2: {solution2}")