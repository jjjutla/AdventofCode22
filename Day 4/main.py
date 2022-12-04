with open("input.txt") as input:
    lines = input.read().strip().split()
answer1 = 0
answer2 = 0
for line in lines:
    elves = line.split(",")
    ranges = [list(map(int, elf.split("-"))) for elf in elves]
    a, b = ranges[0]
    c, d = ranges[1]
    if a <= c and b >= d or a >= c and b <= d:
        answer1 += 1
    if not (b < c or a > d):
        answer2 += 1
print("Part 1:",answer1)
print("Part 2:",answer2)