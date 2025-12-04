path = './data.txt'

roll_map = []
with open(path, "r") as file:
    for line in file:
        roll_map.append("." + line.strip() + ".")

roll_map.insert(0, "." * len(roll_map[0]))
roll_map.append("." * len(roll_map[0]))

result = 0
for r in range(1, len(roll_map) - 1):
    for c in range(1, len(roll_map[0]) - 1):
        if roll_map[r][c] != "@": continue
        count = 0
        count += roll_map[r - 1][c - 1] == "@"
        count += roll_map[r - 1][c]     == "@"
        count += roll_map[r - 1][c + 1] == "@"
        count += roll_map[r][c - 1] == "@"
        count += roll_map[r][c + 1] == "@"
        count += roll_map[r + 1][c - 1] == "@"
        count += roll_map[r + 1][c] == "@"
        count += roll_map[r + 1][c + 1] == "@"
        result += count < 4

print(result)
