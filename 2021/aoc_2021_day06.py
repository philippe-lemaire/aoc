# aoc 2021 day 6

import numpy as np


def get_lanternfish_small():
    return [3, 4, 3, 1, 2]


def get_lanternfish_full():
    data = [
        1,
        4,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        4,
        3,
        1,
        1,
        3,
        5,
        1,
        5,
        3,
        2,
        1,
        1,
        2,
        3,
        1,
        1,
        5,
        3,
        1,
        5,
        1,
        1,
        2,
        1,
        2,
        1,
        1,
        3,
        1,
        5,
        1,
        1,
        1,
        3,
        1,
        1,
        1,
        1,
        1,
        1,
        4,
        5,
        3,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        1,
        1,
        1,
        1,
        4,
        4,
        4,
        1,
        1,
        1,
        1,
        5,
        1,
        2,
        4,
        1,
        1,
        4,
        1,
        2,
        1,
        1,
        1,
        2,
        1,
        5,
        1,
        1,
        1,
        3,
        4,
        1,
        1,
        1,
        3,
        2,
        1,
        1,
        1,
        4,
        1,
        1,
        1,
        5,
        1,
        1,
        4,
        1,
        1,
        2,
        1,
        4,
        1,
        1,
        1,
        3,
        1,
        1,
        1,
        1,
        1,
        3,
        1,
        3,
        1,
        1,
        2,
        1,
        4,
        1,
        1,
        1,
        1,
        3,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        1,
        3,
        1,
        1,
        1,
        1,
        4,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        1,
        1,
        5,
        1,
        1,
        1,
        2,
        2,
        1,
        1,
        3,
        5,
        1,
        1,
        1,
        1,
        3,
        1,
        3,
        3,
        1,
        1,
        1,
        1,
        3,
        5,
        2,
        1,
        1,
        1,
        1,
        5,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        1,
        2,
        1,
        1,
        1,
        2,
        1,
        1,
        1,
        1,
        1,
        2,
        1,
        1,
        1,
        1,
        1,
        5,
        1,
        4,
        3,
        3,
        1,
        3,
        4,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        4,
        3,
        5,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        5,
        2,
        1,
        4,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        5,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        1,
        4,
        4,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        5,
        1,
        1,
        2,
        5,
        1,
        1,
        4,
        1,
        3,
        1,
        1,
    ]
    return data


def generate_lanternfish(days, size):
    """naive approach, doing it like it's shown, by accounting for each fish in a list"""
    if size == "small":
        lanternfish = get_lanternfish_small()
    else:
        lanternfish = get_lanternfish_full()
    for day in range(1, days + 1):
        new_fish = []
        old_fish = []
        for l in lanternfish:
            if l > 0:
                old_fish.append(l - 1)
            else:
                old_fish.append(6)
                new_fish.append(8)
        # reassemble the fish
        lanternfish = old_fish + new_fish
        # print(f"After {day} day(s): {str(lanternfish)}")
    return len(lanternfish)


print(f"{generate_lanternfish(days=80, size='small')=}")

print(f"{generate_lanternfish(days=80, size='full')=}")

## Part 2

# new implementation with np.arrays, but similar to previous one
def generate_lanternfish(days, size):
    """New version, with numpy arrays instead of lists"""
    if size == "small":
        lanternfish = get_lanternfish_small()
        lanternfish = np.array(lanternfish)
    else:
        lanternfish = get_lanternfish_full()
        lanternfish = np.array(lanternfish)
    for day in range(1, days + 1):
        lanternfish = lanternfish - 1
        new = len(lanternfish[lanternfish < 0])
        lanternfish[lanternfish < 0] = 6
        new_fish = np.array([8] * new)
        # reassemble the fish
        lanternfish = np.concatenate((lanternfish, new_fish))
        # print(f"After {day} days, {len(lanternfish)} fish.")
    return len(lanternfish)


print(f"{generate_lanternfish(days=80, size='full')=}")

# part 2 - smarter

"""
the naive methods used before explodes when doing more than 200 days.

but we can compress the information we have: all we need is to count how many fish we have of each age

make that into a length 9 list. The position in the list is the age, the numbers in the list are how many fish we have for each age.

And each day, shift the counts one index to the left to make them age one day.
"""

from collections import Counter


def count_fish(fish, days):
    # the counter_list will hold how many fish there are of age i in counter_list[i]
    # start with a list of zeros, one for each possible age between 0 and 8
    counter_list = [0] * 9
    # get the initial count thanks to counter
    c = Counter(fish)
    for k in c:
        counter_list[k] = c.get(k)
    # our day to day logic
    for day in range(days):
        # we get how many fish are at 0 days + we shift the whole list one position by poping index 0
        new_fish = counter_list.pop(0)
        # add the new fish at the end of the list (8th index)
        counter_list.append(new_fish)
        # the fish that just reproduced are added to the 6 days fish
        counter_list[6] += new_fish
        # repeat once per day
    return sum(counter_list)


fish = get_lanternfish_full()
print(f"Final tally = {count_fish(fish, 256)}")
