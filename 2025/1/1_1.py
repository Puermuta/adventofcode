path = "./data.txt"

dial = 50
result = 0 

with open(path, "r") as file:
    for line in file:
        if line[1:] == "": continue
        if line[0] == "R":
            dial += int(line[1:])
        else:
            dial -= int(line[1:])

        result += dial%100 == 0  

print(result)

