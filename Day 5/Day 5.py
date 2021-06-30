import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)  

def parse(inp):
    input = []
    for line in inp:
        if line != "\n":
            input.append(line)
    return input
    
file = open("Day 5/input.txt")
input = parse(file)
file.close()

max = 0
plane = np.zeros((127,8))

for line in input:
    lower_row = 0
    upper_row = 127
    lower_col = 0
    upper_col = 7
    row = 0
    col = 0
    for char in line:
        if char == 'F':
            upper_row = int((upper_row-lower_row-1)/2+lower_row)
        elif char == 'B':
            lower_row = int((upper_row-lower_row+1)/2+lower_row)
        if char == 'L':
            upper_col = int((upper_col-lower_col-1)/2+lower_col)
        elif char == 'R':
            lower_col = int((upper_col-lower_col+1)/2+lower_col)
    if lower_row == upper_row:
        row = lower_row
    if lower_col == upper_col:
        col = lower_col
    id = row*10+col
    plane[row][col] = id
for row in range(len(plane)):
    for col in range(len(plane[row])):
        if plane[row][col] == 0:
            print(row, col, 8*row + col)