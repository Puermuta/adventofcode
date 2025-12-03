path = "./data.txt"

total = 0
with open(path, "r") as file:
    for line in file:
        bank = [int(n) for n in line.strip()]
        
        n = len(bank)
        stack = []
        to_remove = n - 12
        for battery in bank:
            while stack and to_remove > 0 and stack[-1] < battery:
                stack.pop()
                to_remove -= 1
            stack.append(battery)

        result = 0
        for p, battery in enumerate(stack[:12]):
            result += battery * 10 ** (11 - p)
        
        total += result

print(total)
