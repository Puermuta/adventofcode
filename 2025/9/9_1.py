path = './data.txt'

data = [tuple(map(int, (a.strip()).split(","))) for a in open(path)]

max_size = 0

for first in data:
    for second in data:
        area = (abs(first[0] - second[0]) + 1) * (abs(first[1] - second[1]) + 1)
        max_size = max(max_size, area)

print(max_size)
