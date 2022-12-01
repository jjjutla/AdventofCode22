with open("input.txt", "r") as data:
    totalSum = []
    sectionSum = 0
    for number in data:
        if number != "\n":
            sectionSum = sectionSum + int(number)
        else:
            totalSum.append(sectionSum)
            sectionSum = 0
totalSum.sort(reverse=True)
print("Part 1:", totalSum[0])
print("Part 2:", totalSum[0] + totalSum[1] + totalSum[2])
