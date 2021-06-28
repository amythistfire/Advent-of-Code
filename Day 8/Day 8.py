import re
from pprint import pprint

test = False

filename = "input.txt"
if test:
    filename = "input_test.txt"

with open(filename) as f:
    lines = f.read().splitlines()

execute = set()
it = 0
acc = 0

done = False

while not done:
    line = lines[it]
    inst = line[0:3]
    char = int(line[4:])
    if inst == "nop":
        it+=1
    elif inst == "acc":
        acc += char
        it+=1
    elif inst == "jmp":
        it+=char
    if it in execute:
        done = True
    else:
        execute.add(it)

print(f"Part 1: {acc}")

lines_orig = lines.copy()
finished = False
changed_set = set()
while not finished:
    lines = lines_orig.copy()
    changed = 0
    execute = set()
    it = 0
    acc = 0
    done = False
    while not done and it < len(lines_orig):
        line = lines[it]
        inst = line[0:3]
        char = int(line[4:])
        if inst == "nop":
            if it not in changed_set and changed == 0:
                changed = it
                changed_set.add(it)
                line = "jmp"
                it += char
            else:
                it+=1
        elif inst == "acc":
            acc += char
            it+=1
        elif inst == "jmp":
            if it not in changed_set and changed == 0:
                changed = it
                changed_set.add(it)
                line = "nop"
                it += 1
            else:
                it+=char
        if it in execute:
            print(changed)
            done = True
        else:
            execute.add(it)
    if it >= len(lines_orig):
        finished = True
print(f"Part 2: {acc}")