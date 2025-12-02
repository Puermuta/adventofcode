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

            found_ids = set()

            for number in range(first, second + 1):
                number = str(number)
                for splits in range(2, len(number) + 1):

                    if len(number) % splits != 0:
                        continue
                    
                    disp_number = number
                    split_index = len(number) // splits
                    substring = disp_number[:split_index]

                    found = True
                    while disp_number != "":
                        if substring != disp_number[:split_index]:
                            found = False
                            break
                        else:
                            substring = disp_number[:split_index]
                            disp_number = disp_number[split_index:]
                            

                    if found and number not in found_ids:
                        bignumber += int(number)
                        found_ids.add(number)

print(bignumber)