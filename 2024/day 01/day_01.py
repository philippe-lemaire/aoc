# data reading


with open("input.txt") as f:
    data = f.readlines()

list1 = []
list2 = []

for line in data:
    a, b = line.split()
    list1.append(int(a))
    list2.append(int(b))

# Part 1
result_part_1 = sum(abs(a - b) for a, b in zip(sorted(list1), sorted(list2)))

print(f"The result for part 1 is {result_part_1}")

# Part 2
score = 0
from collections import Counter

c = Counter(list2)

for k in list1:
    score += k * c.get(k, 0)

print(f"The result for part 2 is {score}")
