def parse(inp):
    input = []
    group = ""
    for line in inp:
        if line != "\n":
            group += line
        else:
            input.append(group)
            group = ""
    return input
    
file = open("Day 6/input.txt")
input = parse(file)
file.close()

sum = 0
for group in input:
    total = 0
    for c in range(ord('a'), ord('z')+1):
        char = chr(c)
        if char in group:
            total += 1
    sum += total

print(sum)

sum = 0
for group in input:
    lines = group.splitlines()
    total = 0
    for c in range(ord('a'), ord('z')+1):
        char = chr(c)
        every = True
        for line in lines:
            if (char in line and every):
                every = True
            else:
                every = False
        if every:
            total += 1
    sum += total

print(sum)