arr = [3, 4, -1, 1]

num_set = set(arr)
smallest = 1

while smallest in num_set:
    smallest += 1

print("Smallest missing positive integer:", smallest)