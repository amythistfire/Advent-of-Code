import re
from pprint import pprint
from copy import deepcopy

test = True

if test:
    filename = "input_test.txt"
else:
    filename = "input.txt"

with open(filename) as f:
    lines = f.read().splitlines()

seats = []
for line in lines:
    seat = []
    for ch in line:
        seat.append(ch)
    seats.append(seat)

orig_seats = deepcopy(seats)

done = False
new_seats = deepcopy(seats)
while not done:
    for x in range(len(seats)):
        for y in range(0, len(seats[x])):
            seat = seats[x][y]
            occupied = 0
            for i in [-1, 0, 1]:
                if 0 <= x + i < len(seats):
                    for j in [-1, 0, 1]:
                        if 0 <= y + j < len(seats[x]):
                            if not (i == j == 0):
                                # print(f"({x},{y}) ({x + i}, {y + j}) {seat}")
                                check = seats[x + i][y + j]
                                if check == '#':
                                    occupied += 1
            if seat == 'L' and occupied == 0:
                new_seats[x][y] = '#'
            if seat == '#' and occupied >= 4:
                new_seats[x][y] = 'L'
    if seats == new_seats:
        done = True
    seats = deepcopy(new_seats)
count = 0
for x in range(len(seats)):
    for y in range(0, len(seats[x])):
        if seats[x][y] == '#':
            count += 1

print(f"Part 1: {count}")

seats = deepcopy(orig_seats)
new_seats = deepcopy(seats)
done = False
for a in range(4):
    for x in range(len(seats)):
        for y in range(0, len(seats[x])):
            seat = seats[x][y]
            occupied = 0
            adj_occupied = 0
            if seat != '.':
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if not (i == j == 0):
                            seen = False
                            for s in range(1, min(len(seats), len(seats[x])), 1):
                                if not seen:
                                    if 0 <= x + s * i < len(seats):
                                        if 0 <= y + s * j < len(seats[x]):
                                            # print(i, j)

                                            check = seats[x + s*i][y + s*j]
                                            print(f"({x},{y}) ({x + s * i}, {y + s * j}) ({seat},{check})")
                                            if check == '#':
                                                occupied += 1
                                                seen = True
                                                if s == 1:
                                                    adj_occupied += 1
                print(seat, occupied, adj_occupied)
                if seat == 'L' and adj_occupied == 0:
                    new_seats[x][y] = '#'
                if seat == '#' and occupied >= 5:
                    new_seats[x][y] = 'L'
                print(new_seats[x][y])
    if seats == new_seats:
        done = True
    pprint(new_seats)
    print("\n")
    seats = deepcopy(new_seats)

count = 0
for x in range(len(seats)):
    for y in range(0, len(seats[x])):
        if seats[x][y] == '#':
            count += 1

print(f"Part 2: {count}")