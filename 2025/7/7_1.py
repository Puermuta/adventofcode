path = './data.txt'

data = [list(line.rstrip("\n")) for line in open(path)]

def project_beam(col: int, row:int, data: list[int], visited: set) -> None:
    while data[row][col] != "^":
        data[row][col] = '|'
        row += 1
        if row == len(data):
            return

    if (row, col) not in visited:
        visited.add((row, col))
        project_beam(col + 1, row, data, visited)
        project_beam(col - 1, row, data, visited)

visited = set()
s = data[0].index("S")
project_beam(s, 1, data, visited)

print(len(visited))
