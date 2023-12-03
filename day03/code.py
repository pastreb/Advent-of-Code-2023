import os.path
import re


def read_input(input_file_name):
    input_file = os.path.join(os.path.dirname(__file__), input_file_name)
    with open(input_file, "r") as f:
        input = []
        for line in f.readlines():
            input.append(list(line.replace("\n", "")))
        return input


# --- Day 3: Gear Ratios ---
# You and the Elf eventually reach a gondola lift station; he says the
# gondola lift will take you up to the water source, but this is as far as he
# can bring you. You go inside.

# It doesn't take long to find the gondolas, but there seems to be a problem:
# they're not moving.

# "Aaah!"

# You turn around to see a slightly-greasy Elf with a wrench and a look of
# surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working
# right now; it'll still be a while before I can fix it." You offer to help.

# The engineer explains that an engine part seems to be missing from the
# engine, but nobody can figure out which one. If you can add up all the part
# numbers in the engine schematic, it should be easy to work out which part
# is missing.

# The engine schematic (your puzzle input) consists of a visual
# representation of the engine. There are lots of numbers and symbols you
# don't really understand, but apparently any number adjacent to a symbol,
# even diagonally, is a "part number" and should be included in your sum.
# (Periods (.) do not count as a symbol.)

# Here is an example engine schematic:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

# In this schematic, two numbers are not part numbers because they are not
# adjacent to a symbol: 114 (top right) and 58 (middle right). Every other
# number is adjacent to a symbol and so is a part number; their sum is 4361.

# Of course, the actual engine schematic is much larger. What is the sum of all of
# the part numbers in the engine schematic?


def check_if_symbol(input, i, j):
    if (
        i >= 0 and i < len(input) and j >= 0 and j < len(input[i])
    ):  # check if element exists
        return (not input[i][j].isdigit()) and input[i][
            j
        ] != "."  # check if element is symbol
    return False


def check_adjacent_symbols(input, i, j):
    if check_if_symbol(input, i - 1, j):
        return True  # Symbol above digit at i, j
    if check_if_symbol(input, i + 1, j):
        return True  # Symbol below digit at i, j
    if check_if_symbol(input, i, j - 1):
        return True  # Symbol left of digit at i, j
    if check_if_symbol(input, i, j + 1):
        return True  # Symbol right of digit at i, j
    if check_if_symbol(input, i - 1, j - 1):
        return True  # Symbol on top-left diagonal of digit at i, j
    if check_if_symbol(input, i - 1, j + 1):
        return True  # Symbol on top-right diagonal of digit at i, j
    if check_if_symbol(input, i + 1, j - 1):
        return True  # Symbol on bottom-left diagonal of digit at i, j
    if check_if_symbol(input, i + 1, j + 1):
        return True  # Symbol on bottom-right diagonal of digit at i, j
    return False


def compute_part_1(input_file_name="input.txt"):
    input = read_input(input_file_name)
    sum = 0
    for i in range(len(input)):
        j = 0
        while j < len(input[i]):
            if input[i][j].isdigit():  # start of digit
                digit = ""
                has_symbol = False
                while j < len(input[i]) and input[i][j].isdigit():
                    digit += input[i][j]
                    has_symbol = has_symbol or check_adjacent_symbols(input, i, j)
                    j += 1
                if has_symbol:
                    sum += int(digit)
            j += 1
    return sum


# Your puzzle answer was 525911.

# --- Part Two ---
# The engineer finds the missing part and installs it in the engine! As the
# engine springs to life, you jump in the closest gondola, finally ready to
# ascend to the water source.

# You don't seem to be going very fast, though. Maybe something is still
# wrong? Fortunately, the gondola has a phone labeled "help", so you pick it
# up and the engineer answers.

# Before you can explain the situation, she suggests that you look out the
# window. There stands the engineer, holding a phone in one hand and waving
# with the other. You're going so slowly that you haven't even left the
# station. You exit the gondola.

# The missing part wasn't the only issue - one of the gears in the engine is
# wrong. A gear is any * symbol that is adjacent to exactly two part numbers.
# Its gear ratio is the result of multiplying those two numbers together.

# This time, you need to find the gear ratio of every gear and add them all up
# so that the engineer can figure out which gear needs to be replaced.

# Consider the same engine schematic again:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

# In this schematic, there are two gears. The first is in the top left; it
# has part numbers 467 and 35, so its gear ratio is 16345. The second gear is
# in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not
# a gear because it is only adjacent to one part number.) Adding up all of
# the gear ratios produces 467835.

# What is the sum of all of the gear ratios in your engine schematic?

visited = []


def try_to_get_entire_number(input, i, j):
    if not input[i][j].isdigit():
        return ""
    global visited
    while j - 1 >= 0 and input[i][j - 1].isdigit():
        j -= 1
    number = ""
    while j < len(input[i]) and input[i][j].isdigit():
        number += input[i][j]
        visited.append([i, j])
        j += 1
    return number


def find_adjacent_numbers(input, i, j):
    global visited
    adjacent_numbers = []
    visited = (
        []
    )  # to prevent duplicates of the same number (note that "equal numbers are possible, e.g. 42*42")
    for neighbor in [
        [i - 1, j],
        [i + 1, j],
        [i, j - 1],
        [i, j + 1],
        [i - 1, j - 1],
        [i - 1, j + 1],
        [i + 1, j - 1],
        [i + 1, j + 1],
    ]:
        if not [neighbor[0], neighbor[1]] in visited:
            adjacent_number = try_to_get_entire_number(input, neighbor[0], neighbor[1])
            if adjacent_number.isdigit():
                adjacent_numbers.append(int(adjacent_number))
    return adjacent_numbers


def compute_part_2(input_file_name="input.txt"):
    input = read_input(input_file_name)
    sum = 0
    for i in range(len(input)):
        for j in range(len(input)):
            if input[i][j] == "*":
                adjacent_numbers = find_adjacent_numbers(input, i, j)
                if len(adjacent_numbers) == 2:
                    sum += adjacent_numbers[0] * adjacent_numbers[1]
    return sum


# Your puzzle answer was 75805607.

if __name__ == "__main__":
    print(f"PART 1: {compute_part_1()}")
    print(f"PART 2: {compute_part_2()}")
