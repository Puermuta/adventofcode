import re

path = "./data.txt"

pattern = re.compile(r'(.+?)\1')

bignumber = 0
with open(path, "r") as file:
    for line in file:
        
        while len(line) > 0:
            dash = line.find("-")
            comma = line.find(",")
            first = int(line[:dash])
            
            
            if comma == -1:
                second = int(line[dash + 1:])
                line = "" 
            else:
                second = int(line[dash + 1:comma])
                line = line[comma + 1:]

            for number in range(first, second + 1):
                number = str(number)
                if len(number) % 2 == 1:
                    continue
                
                split_index = len(number) // 2
                if number[:split_index] == number[split_index:] and number[0] != 0:
                    bignumber += int(number)

print(bignumber)