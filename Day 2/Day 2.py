import re

file = open("Day 2/input.txt")
list = []
for line in file:
    list.append(line.strip())
file.close()

correct1 = 0
correct2 = 0

min = 0
max = 0
check = 'm'
phrase = " mrfmmbjxr"
count = 0
for item in list:
    count = 0
    spec = re.split(":", item)[0]
    str = re.split(":", item)[1]

    min = int(re.findall("[0-9]+", spec)[0])
    max = int(re.findall("[0-9]+", spec)[1])
    check = re.findall("[a-z]", spec)[0]

    for letter in str:
        if letter == check:
            count += 1

    if min <= count <= max:
        correct1 += 1

    print(check, str[min], str[max])
    if (check == str[min] or check == str[max]) and not (check == str[min] and check == str[max]):
        correct2 += 1
    
print(correct1)
print(correct2)
