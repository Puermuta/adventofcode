from collections import deque
path = './test_data.txt'

result = 0
with open(path, 'r') as file:
    iteration = 1
    for line in file:
        print(iteration)
        line = line.split()
        joltages = list(map(int, line[-1].strip("{}").split(",")))
        N_lights = len(line[0][1:-1])
        buttons = []
        for button in line[1:-1]:
            indices = tuple(map(int, button.strip("()").split(",")))
            array_button = [0] * N_lights
            for idx in indices:
                array_button[idx] = 1
            buttons.append(array_button) 

        visited = set()
        queue = deque()
        queue.append((tuple([0] * N_lights), 0))
        found = False
        while not found:
            current, steps = queue.popleft()
            for button in buttons:
                pressed = [x + y for x, y in zip(current, button)]
                if any(a > b for a, b in zip(pressed, joltages)):
                    continue
                if pressed == joltages:
                    found = True
                    result += steps + 1
                    break
                
                if tuple(pressed) not in visited:
                    print(len(queue))
                    visited.add(tuple(pressed))
                    queue.append((pressed, steps + 1))

        iteration += 1

print(result)

        
        


