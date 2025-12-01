path = "./data.txt"

dial = 50
result = 0


with open(path, "r") as file:
    for line in file:
        if line[1:] == "": continue

        move = int(line[1:])

        if line[0] == "R":
            for i in range(move):
                dial += 1
                dial %= 100
                result += dial == 0
        else:
            for i in range(move):
                dial -= 1
                dial %= 100
                result += dial == 0

print(result)
