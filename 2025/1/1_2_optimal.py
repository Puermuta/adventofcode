path = "./data.txt"

dial = 50
result = 0

with open(path, "r") as file:
    for line in file:
        if line[1:] == "": continue

        move = int(line[1:])

        if line[0] == "R":
            result += (dial + move) // 100
            dial = (dial + move) % 100
        else:
            result += ((100 - dial) % 100 + move) // 100
            dial = (dial - move) % 100

print(result)
