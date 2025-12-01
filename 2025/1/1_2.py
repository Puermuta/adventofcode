path = "./data.txt"

dial = 50
result = 0
rights = 0
lefts = 0

with open(path, "r") as file:
    for line in file:
        if line[1:] == "": continue

        move = int(line[1:])

        if line[0] == "R":
            for i in range(move):
                dial += 1
                dial %= 100
                result += dial == 0
                rights += dial == 0
        else:
            print(move)
            for i in range(move):
                dial -= 1
                dial %= 100
                result += dial == 0
                lefts += dial == 0

print(result, rights, lefts)
