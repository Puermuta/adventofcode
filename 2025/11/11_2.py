"""
Solution for https://adventofcode.com/2025/day/11 part 2.
Solved using a DFS search and dynamic programming.
Time complexity of O(N), where N is the amount of nodes
in the graph.
"""
from collections import deque

path = "./data.txt"

graph = dict()

with open(path, "r") as file:
    for line in file:
        parts = line.split()
        graph[parts[0][:-1]] = parts[1:]

memo = dict()
def dfs_memo(node, dac, fft):
    dac = dac or (node == "dac")
    fft = fft or (node == "fft")

    if node == "out":
        return dac and fft

    if (node, dac, fft) not in memo:
        memo[(node, dac, fft)] = 0
    else:
        return memo[(node, dac, fft)]

    for child in graph[node]:
        memo[(node, dac, fft)] += dfs_memo(child, dac, fft)

    return memo[(node, dac, fft)]
    
print(dfs_memo("svr", 0, 0))
