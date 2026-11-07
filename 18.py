intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]

intervals.sort()

merged = [intervals[0]]

for start, end in intervals[1:]:
    last = merged[-1]

    if start <= last[1]:
        last[1] = max(last[1], end)
    else:
        merged.append([start, end])

print("Merged intervals:", merged)