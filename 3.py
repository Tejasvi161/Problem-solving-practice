arr = [0, 1, 0, 3, 12, 0, 5]

result = []

for num in arr:
    if num != 0:
        result.append(num)

zeros = arr.count(0)

result.extend([0] * zeros)

print(result)