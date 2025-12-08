path = './data.txt'

points = dict([(tuple(map(int, (a.strip()).split(','))), -1) for a in open(path)])

distances = []
visited = set()
for point in points:
    distance = {}
    for other in points:
        if point == other or (other, point) in visited:
            continue
        dx = point[0] - other[0]
        dy = point[1] - other[1]
        dz = point[2] - other[2]
        distances.append((dx*dx + dy*dy + dz*dz, point, other))
        visited.add((point, other))
distances.sort(reverse = True)

groups = []
while distances:
    a, b = distances[-1][1:3]
    change = True
    if points[a] == -1 and points[b] == -1:
        groups.append([a, b])
        points[a] = len(groups) - 1
        points[b] = len(groups) - 1
    elif points[a] != -1 and points[b] == -1:
        group = points[a]
        groups[group].append(b)
        points[b] = group
    elif points[b] != -1 and points[a] == -1:
        group = points[b]
        groups[group].append(a)
        points[a] = group
    elif points[a] != points[b]:
        (small_group, big_group) = (points[a], points[b]) if len(groups[points[b]]) > len(groups[points[a]]) else (points[b], points[a])
        
        for point in groups[small_group]:
            points[point] = big_group

        groups[big_group] += groups[small_group]
        groups[small_group] = []
    else:
        change = False

    if change:
        lastA, lastB = a, b

    distances.pop()

result = lastA[0] * lastB[0]
print(result)
