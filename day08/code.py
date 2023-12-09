import os.path
import re
import math


def read_input(input_file_name):
    input_file = os.path.join(os.path.dirname(__file__), input_file_name)
    with open(input_file, "r") as f:
        lines = f.readlines()
        return lines


class Dummy:
    def __init__(self):
        self.dummy = 0

    def setup(self, input):
        for set in re.findall(r"[^;]+", input):
            pass


# --- Day 8: Haunted Wasteland ---
# You're still riding a camel across Desert Island when you spot a sandstorm
# quickly approaching. When you turn to warn the Elf, she disappears before
# your eyes! To be fair, she had just finished warning you about ghosts a few
# minutes ago.

# One of the camel's pouches is labeled "maps" - sure enough, it's full of
# documents (your puzzle input) about how to navigate the desert. At least,
# you're pretty sure that's what they are; one of the documents contains a
# list of left/right instructions, and the rest of the documents seem to
# describe some kind of network of labeled nodes.

# It seems like you're meant to use the left/right instructions to navigate
# the network. Perhaps if you have the camel follow the same instructions,
# you can escape the haunted wasteland!

# After examining the maps for a bit, two nodes stick out: AAA and ZZZ. You
# feel like AAA is where you are now, and you have to follow the left/right
# instructions until you reach ZZZ.

# This format defines each node of the network individually. For example:

# RL

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)

# Starting with AAA, you need to look up the next element based on the next
# left/right instruction in your input. In this example, start with AAA and
# go right (R) by choosing the right element of AAA, CCC. Then, L means to
# choose the left element of CCC, ZZZ. By following the left/right
# instructions, you reach ZZZ in 2 steps.

# Of course, you might not find ZZZ right away. If you run out of left/right
# instructions, repeat the whole sequence of instructions as necessary: RL
# really means RLRLRLRLRLRLRLRL... and so on. For example, here is a
# situation that takes 6 steps to reach ZZZ:

# LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)

# Starting at AAA, follow the left/right instructions. How many steps are
# required to reach ZZZ?


def get_instructions_and_maps(input):
    instructions = re.match(r"\w+", input[0]).group(0)
    maps = {}
    for line in input:
        matches = re.match(r"(\w+)\s*=\s*\((\w+),\s*(\w+)\)", line)
        if matches:
            maps[matches.group(1)] = [matches.group(2), matches.group(3)]
    return instructions, maps


def compute_part_1(input_file_name="input.txt"):
    input = read_input(input_file_name)
    instructions, maps = get_instructions_and_maps(input)
    current_node = "AAA"
    i = 0
    while current_node != "ZZZ":
        current_node = maps[current_node][
            0 if (instructions[i % len(instructions)] == "L") else 1
        ]
        i += 1
    return i


# Your puzzle answer was 18673.

# --- Part Two ---
# The sandstorm is upon you and you aren't any closer to escaping the
# wasteland. You had the camel follow the instructions, but you've barely
# left your starting position. It's going to take significantly more steps to
# escape!

# What if the map isn't for people - what if the map is for ghosts? Are
# ghosts even bound by the laws of spacetime? Only one way to find out.

# After examining the maps a bit longer, your attention is drawn to a curious
# fact: the number of nodes with names ending in A is equal to the number
# ending in Z! If you were a ghost, you'd probably just start at every node
# that ends with A and follow all of the paths at the same time until they
# all simultaneously end up at nodes that end with Z.

# For example:

# LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)

# Here, there are two starting nodes, 11A and 22A (because they both end with
# A). As you follow each left/right instruction, use that instruction to
# simultaneously navigate away from both nodes you're currently on. Repeat
# this process until all of the nodes you're currently on end with Z. (If
# only some of the nodes you're on end with Z, they act like any other node
# and you continue as normal.) In this example, you would proceed as follows:

# Step 0: You are at 11A and 22A.
# Step 1: You choose all of the left paths, leading you to 11B and 22B.
# Step 2: You choose all of the right paths, leading you to 11Z and 22C.
# Step 3: You choose all of the left paths, leading you to 11B and 22Z.
# Step 4: You choose all of the right paths, leading you to 11Z and 22B.
# Step 5: You choose all of the left paths, leading you to 11B and 22C.
# Step 6: You choose all of the right paths, leading you to 11Z and 22Z.

# So, in this example, you end up entirely on nodes that end in Z after 6
# steps.

# Simultaneously start on every node that ends with A. How many steps does it
# take before you're only on nodes that end with Z?


def check_done(current_nodes):
    for node in current_nodes:
        if not node[2] == "Z":
            return False
    return True


def compute_part_2(input_file_name="input.txt"):
    input = read_input(input_file_name)
    instructions, maps = get_instructions_and_maps(input)
    current_nodes = [x for x in maps.keys() if x[2] == "A"]
    first_times_z = []
    for current_node in current_nodes:
        i = 0
        while current_node[2] != "Z":
            current_node = maps[current_node][
                0 if (instructions[i % len(instructions)] == "L") else 1
            ]
            i += 1
        first_times_z.append(i)
    return math.lcm(*first_times_z)


# Your puzzle answer was 17972669116327.

if __name__ == "__main__":
    print(f"PART 1: {compute_part_1()}")
    print(f"PART 2: {compute_part_2()}")
