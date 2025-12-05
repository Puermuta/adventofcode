path = './data.txt'

"""
Naive solution because it just works fine.
"""

result = 0
ranges = []
with open(path, 'r') as file:
    for line in file:
        if line.strip() == "": break
        start, end = map(int, line.strip().split('-'))
        ranges.append((start, end))
    ranges.sort()
    for line in file:
        number = int(line.strip())
        for start, end in ranges:
            if start <= number and number <= end:
                result += 1
                break

print(result)
