path = './data.txt'

'''
Very simple and effective.
'''

data = []
operators = []
with open(path, 'r') as file:
    for line in file:
        line = line.strip()
        try:
            int(line[0])
            data.append(list(map(int, line.split())))
        except:
            operators = list(line.split())

result = 0
for col, operator in enumerate(operators):
    total = 0
    for row in range(len(data)):
        num = data[row][col]
        match operator:
            case "*":
                if total == 0: 
                    total = num
                else:
                    total *= num
            case "+":
                total += num
    result += total

print(result)
