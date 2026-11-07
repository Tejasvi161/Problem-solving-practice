arr = [1, 2, 3, -2, 2]
k = 3

count = 0
prefix_sum = 0
freq = {0: 1}

for num in arr:
    prefix_sum += num

    if prefix_sum - k in freq:
        count += freq[prefix_sum - k]

    freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

print("Number of subarrays:", count)