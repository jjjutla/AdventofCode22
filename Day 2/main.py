score = 0
possibleOutcomes = {
    "A X":4, "A Y":8, "A Z":3, 
    "B X":1, "B Y":5, "B Z":9,
    "C X":7, "C Y":2, "C Z":6
}
newPossibleOutcomes = {
    "A X":3, "A Y":4, "A Z":8, 
    "B X":1, "B Y":5, "B Z":9,
    "C X":2, "C Y":6, "C Z":7
} 
with open("input.txt") as file:
    rounds = [i for i in file.read().strip().split("\n")]
for i in rounds:
    score = score + possibleOutcomes[i]
print("Part 1:", score)
score = 0
for i in rounds:
    score = score + newPossibleOutcomes[i]
print("Part 2:", score)
score = 0