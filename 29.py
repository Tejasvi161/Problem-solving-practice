arr = [2, 3, 1, 1, 4]

jumps = 0
current_end = 0
farthest = 0

for i in range(len(arr) - 1):
    farthest = max(farthest, i + arr[i])

    if i == current_end:
        jumps += 1
        current_end = farthest

print("Minimum jumps required:", jumps)