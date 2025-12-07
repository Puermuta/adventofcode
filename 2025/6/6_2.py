from math import prod
path = './data.txt'

'''
Maybe not optimal, but it works.
'''

data = []
operators = []
with open(path, 'r') as file:
    for line in file:
        line = line.strip()
        try:
            int(line[0])
            data.append(list(line))
        except:
            operators = list(line)

result = 0
for col in range(len(operators)):
    if operators[col] != " ":
        just_spaces = False
        cc = col
        numbers = []
        while not just_spaces:
            just_spaces = True
            number = ''
            for row in range(len(data)):
                total = 0
                try:
                    int(data[row][cc])
                    just_spaces = False
                    number += data[row][cc]
                except:
                    continue
            cc += 1
            if not just_spaces: numbers.append(int(number))
        pprint(numbers)
        match operators[col]:
            case "*":
                result += prod(numbers)
            case "+":
                result += sum(numbers)
            

print(result)
