import re
from pprint import pprint

test = False

filename = "input.txt"
if test:
    filename = "input_test.txt"

with open(filename) as f:
    lines = f.read().splitlines()


class Bags:
    def __init__(self, color):
        self.color = color
        self.contains = {}
        self.is_contained = {}
    def __repr__(self):
        return f"{color}-{self.contains}-{self.is_contained}"
    color = ""
    contains = {}
    is_contained = {}

bag_dict = {}

for line in lines:

    color_search = '.*(?= bags )'
    color = re.search(color_search, line).group(0)
    if color in bag_dict:
        bag = bag_dict[color]
    else:
        bag = Bags(color)
    contains_search = '(?<=contain ).* bag(s)?(?=.)'
    try:
        contains = re.search(contains_search, line).group(0).split(",")
    except:
        continue
    else:
        bag_dict[color] = bag
        for contain in contains:
            if contain != "no other bags":
                contain_quantity_search = '\d'
                contain_color_search = '(?<=\d ).*(?= bag)'
                quant = re.search(contain_quantity_search, contain).group(0)
                contain_color = re.search(contain_color_search, contain).group(0)

                bag_dict[color].contains[contain_color] = quant
                if contain_color not in bag_dict:
                    bag_dict[contain_color] = Bags(contain_color)
                bag_dict[contain_color].is_contained[color] = quant

def part1(color, contains_dict):
    contains_dict[color] = 1
    for contains_color in bag_dict[color].is_contained:
        part1(contains_color, contains_dict)
    return contains_dict

solution1 = len(part1("shiny gold", {}))-1

def part2(color):
    sum = 1
    for contains_color in bag_dict[color].contains:
        quantity = int(bag_dict[color].contains[contains_color])
        sum += quantity * part2(contains_color)
    return sum

solution2 = part2("shiny gold") - 1
print(f"Part 1 {solution1}")
print(f"Part 2 {solution2}")