path = "./data.txt"

total = 0
with open(path, "r") as file:
    for line in file:
        nums = [int(n) for n in line.strip()]

        first_num = max(nums[:-1])
        first_num_idx = nums.index(first_num)
        second_num = max(nums[first_num_idx + 1:])
        num = first_num * 10 + second_num
        total += num

print(total)
