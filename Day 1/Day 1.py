file = open("input.txt")
list = []
for line in file:
    list.append(int(line.strip()))
file.close()

list.sort()
a=0
b=-1
while (list[a] + list[b] != 2020):
    if list[a] + list[b] > 2020:
        b -= 1
    elif list[a] + list[b] < 2020:
        a += 1
print(list[a], list[b], list[a]*list[b])

a=0
b=199
c=198

while (list[a] + list[b] + list[c] != 2020):
    if list[a] + list[b] + list[c] > 2020:
        if c <= a:
            b -= 1
            c = b - 1
        else:
            c -= 1
    if list[a] + list[b] + list[c] < 2020:
        a += 1
        c = b - 1
        while list[a] + list[b] + list[c] < 2020:
            b += 1
print(list[a], list[b], list[c], list[a]*list[b]*list[c])