import os.path
import re


def read_input(input_file_name):
    input_file = os.path.join(os.path.dirname(__file__), input_file_name)
    with open(input_file, "r") as f:
        lines = f.readlines()
        return lines


# --- Day 14: Parabolic Reflector Dish ---
# You reach the place where all of the mirrors were pointing: a massive
# parabolic reflector dish attached to the side of another large mountain.

# The dish is made up of many small mirrors, but while the mirrors themselves
# are roughly in the shape of a parabolic reflector dish, each individual
# mirror seems to be pointing in slightly the wrong direction. If the dish is
# meant to focus light, all it's doing right now is sending it in a vague
# direction.

# This system must be what provides the energy for the lava! If you focus the
# reflector dish, maybe you can go where it's pointing and use the light to
# fix the lava production.

# Upon closer inspection, the individual mirrors each appear to be connected
# via an elaborate system of ropes and pulleys to a large metal platform
# below the dish. The platform is covered in large rocks of various shapes.
# Depending on their position, the weight of the rocks deforms the platform,
# and the shape of the platform controls which ropes move and ultimately the
# focus of the dish.

# In short: if you move the rocks, you can focus the dish. The platform even
# has a control panel on the side that lets you tilt it in one of four
# directions! The rounded rocks (O) will roll when the platform is tilted,
# while the cube-shaped rocks (#) will stay in place. You note the positions
# of all of the empty spaces (.) and rocks (your puzzle input). For example:

# O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....

# Start by tilting the lever so all of the rocks will slide north as
# far as they will go:

# OOOO.#.O..
# OO..#....#
# OO..O##..O
# O..#.OO...
# ........#.
# ..#....#.#
# ..O..#.O.O
# ..O.......
# #....###..
# #....#....

# You notice that the support beams along the north side of the platform are
# damaged; to ensure the platform doesn't collapse, you should calculate the
# total load on the north support beams.

# The amount of load caused by a single rounded rock (O) is equal to the
# number of rows from the rock to the south edge of the platform, including
# the row the rock is on. (Cube-shaped rocks (#) don't contribute to load.)
# So, the amount of load caused by each rock in each row is as follows:

# OOOO.#.O.. 10
# OO..#....#  9
# OO..O##..O  8
# O..#.OO...  7
# ........#.  6
# ..#....#.#  5
# ..O..#.O.O  4
# ..O.......  3
# #....###..  2
# #....#....  1

# The total load is the sum of the load caused by all of the rounded rocks.
# In this example, the total load is 136.

# Tilt the platform so that the rounded rocks all roll north. Afterward, what
# is the total load on the north support beams?


def tilt_north(platform):
    for j in range(len(platform[0])):
        i = len(platform) - 1
        while i > 0:
            if platform[i][j] == "O" and platform[i - 1][j] == ".":
                platform[i][j], platform[i - 1][j] = ".", "O"
                i = len(platform) - 1
            else:
                i -= 1


def compute_load(platform):
    load = 0
    val = 1
    for i in range(len(platform) - 1, -1, -1):
        for j in range(len(platform)):
            load += val if platform[i][j] == "O" else 0
        val += 1
    return load


def compute_part_1(input_file_name="input.txt"):
    input = read_input(input_file_name)
    platform = [[element for element in row if element != "\n"] for row in input]
    tilt_north(platform)
    return compute_load(platform)


# Your puzzle answer was 106517.

# --- Part Two ---
# The parabolic reflector dish deforms, but not in a way that focuses the
# beam. To do that, you'll need to move the rocks to the edges of the
# platform. Fortunately, a button on the side of the control panel labeled
# "spin cycle" attempts to do just that!

# Each cycle tilts the platform four times so that the rounded rocks roll
# north, then west, then south, then east. After each tilt, the rounded
# rocks roll as far as they can before the platform tilts in the next
# direction. After one cycle, the platform will have finished rolling
# the rounded rocks in those four directions in that order.

# Here's what happens in the example above after each of the first few
# cycles:

# After 1 cycle:
# .....#....
# ....#...O#
# ...OO##...
# .OO#......
# .....OOO#.
# .O#...O#.#
# ....O#....
# ......OOOO
# #...O###..
# #..OO#....

# After 2 cycles:
# .....#....
# ....#...O#
# .....##...
# ..O#......
# .....OOO#.
# .O#...O#.#
# ....O#...O
# .......OOO
# #..OO###..
# #.OOO#...O

# After 3 cycles:
# .....#....
# ....#...O#
# .....##...
# ..O#......
# .....OOO#.
# .O#...O#.#
# ....O#...O
# .......OOO
# #...O###.O
# #.OOO#...O

# This process should work if you leave it running long enough, but you're
# still worried about the north support beams. To make sure they'll survive
# for a while, you need to calculate the total load on the north
# support beams after 1000000000 cycles.

# In the above example, after 1000000000 cycles, the total load on the north
# support beams is 64.

# Run the spin cycle for 1000000000 cycles. Afterward, what is the total load
# on the north support beams?


def tilt_east(platform):
    for i in range(len(platform)):
        j = 0
        while j < len(platform[i]) - 1:
            if platform[i][j] == "O" and platform[i][j + 1] == ".":
                platform[i][j], platform[i][j + 1] = ".", "O"
                j = 0
            else:
                j += 1


def tilt_south(platform):
    for j in range(len(platform[0])):
        i = 0
        while i < len(platform) - 1:
            if platform[i][j] == "O" and platform[i + 1][j] == ".":
                platform[i][j], platform[i + 1][j] = ".", "O"
                i = 0
            else:
                i += 1


def tilt_west(platform):
    for i in range(len(platform)):
        j = len(platform) - 1
        while j > 0:
            if platform[i][j] == "O" and platform[i][j - 1] == ".":
                platform[i][j], platform[i][j - 1] = ".", "O"
                j = len(platform) - 1
            else:
                j -= 1


def compute_key(platform):
    key = ""
    for i in range(len(platform)):
        for j in range(len(platform[i])):
            key += platform[i][j]
    return key


def compute_part_2(input_file_name="input.txt"):
    input = read_input(input_file_name)
    platform = [[element for element in row if element != "\n"] for row in input]
    cycle_detection_list = []
    n_iterations = 1000000000
    for i in range(n_iterations):
        key = compute_key(platform)
        val = compute_load(platform)
        if (key, val) in cycle_detection_list:
            last_seen = cycle_detection_list.index((key, val))
            return cycle_detection_list[
                (n_iterations - last_seen) % (i - last_seen) + last_seen
            ][1]
        else:
            cycle_detection_list.append((key, val))
        tilt_north(platform)
        tilt_west(platform)
        tilt_south(platform)
        tilt_east(platform)
        print(len(cycle_detection_list))
    load = 0
    val = 1
    for i in range(len(platform) - 1, -1, -1):
        for j in range(len(platform)):
            load += val if platform[i][j] == "O" else 0
        val += 1
    return load


if __name__ == "__main__":
    print(f"PART 1: {compute_part_1()}")
    print(f"PART 2: {compute_part_2()}")
