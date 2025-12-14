path = './data.txt'

result = 0
with open(path, 'r') as file:
    for line in file:
        line = line.split()
        lights = int(''.join('1' if c == '#' else '0' for c in line[0][1:-1]), 2)
        N_lights = len(line[0][1:-1])
        buttons = []
        for button in line[1:-1]:
            indices = list(map(int, button.strip("()").split(",")))
            binary_button = 0
            for idx in indices:
                binary_button |= 1 << (N_lights - 1 - idx)
            buttons.append(binary_button)

        visited = set()
        queue = [(0, 0)]
        found = False
        while not found:
            current, steps = queue.pop(0)
            for button in buttons:
                pressed = current ^ button
                if pressed == lights:
                    found = True
                    result += steps + 1
                    break

                if pressed not in visited:
                    visited.add(pressed)
                    queue.append((pressed, steps + 1))

print(result)

        
        


