arr = [100, 4, 200, 1, 3, 2]

num_set = set(arr)
longest = 0

for num in num_set:
    if num - 1 not in num_set:
        count = 1
        current = num

        while current + 1 in num_set:
            current += 1
            count += 1

        longest = max(longest, count)

print("Longest consecutive sequence length:", longest)