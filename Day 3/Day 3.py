file = open("Day 3/input.txt")
list = []
for line in file:
    list.append(line.strip())
file.close()

x = 0
y = 0

count = 0
counting = []

changex = 3
changey = 1

while y <= len(list) - 1:
    line = list[y]
    if line[x] == "#":
        count += 1
    y += changey
    x += changex
    if x >= len(line):
        x -= len(line)

print(changex, changey, count)
counting.append(count)
count = 0

x = 0
y = 0
changex = 1
changey = 1

while y <= len(list) - 1:
    line = list[y]
    if line[x] == "#":
        count += 1
    y += changey
    x += changex
    if x >= len(line):
        x -= len(line)

print(changex, changey, count)
counting.append(count)
count = 0

x = 0
y = 0
changex = 5
changey = 1

while y <= len(list) - 1:
    line = list[y]
    if line[x] == "#":
        count += 1
    y += changey
    x += changex
    if x >= len(line):
        x -= len(line)

print(changex, changey, count)
counting.append(count)
count = 0

x = 0
y = 0
changex = 7
changey = 1

while y <= len(list) - 1:
    line = list[y]
    if line[x] == "#":
        count += 1
    y += changey
    x += changex
    if x >= len(line):
        x -= len(line)

print(changex, changey, count)
counting.append(count)
count = 0

x = 0
y = 0
changex = 1
changey = 2

while y <= len(list) - 1:
    line = list[y]
    if line[x] == "#":
        count += 1
    y += changey
    x += changex
    if x >= len(line):
        x -= len(line)

print(changex, changey, count)
counting.append(count)
count = 0

product = 1

for num in counting:
    product *= num
print(product)