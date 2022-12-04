data = open("input.txt", "r").read().split("\n")
total = 0
for item in data:
    half = len(item)//2
    firstHalf = item[:half]
    secondHalf = item[half:]
    sameItem1, = (set(firstHalf) & set(secondHalf))
    if sameItem1 >= "a":
        total = total + (ord(sameItem1) - ord("a") + 1)
    else:
        total = total + (ord(sameItem1) - ord("A") + 27)
print(total)
total = 0


while True:
    try:
        x = input()
        y = input()
        z = input()
    except:
        break
    sameItem2, = set(x) & set(y) & set(z)
    if sameItem2 >= "a":
        total = total + (ord(sameItem2) - ord("a") + 1)
    else:
        total = total + (ord(sameItem2) - ord("A") + 27)
print(total)

    


 