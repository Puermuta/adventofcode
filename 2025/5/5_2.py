path = './data.txt'

"""
Merges the ranges together in a greedy and naive manner.
When a range cant be more merged, the length of it is
added to the result.
"""

result = 0
ranges = []
with open(path, 'r') as file:
    for line in file:
        if line.strip() == "": break
        start, end = map(int, line.strip().split('-'))
        ranges.append([start, end])
    ranges.sort()
    
    current_start, current_end = ranges[0]
    for start, end in ranges:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            result += current_end - current_start + 1
            current_start, current_end = start, end
    
    result += current_end - current_start + 1

print(result)
