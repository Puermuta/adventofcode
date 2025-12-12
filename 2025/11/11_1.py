"""
Solution for https://adventofcode.com/2025/day/11.
Solved using a greedy technique by traversing a graph,
here using DFS for limiting memory usage.
"""

from collections import deque

path = "./data.txt"

graph = dict()

with open(path, "r") as file:
    for line in file:
        parts = line.split()
        graph[parts[0][:-1]] = parts[1:]

queue = deque()
queue.append("you")
result = 0
while queue:
    current = queue.pop()
    if current == "out":
        result += 1
        continue 
    queue.extend(graph[current])
print(result)
