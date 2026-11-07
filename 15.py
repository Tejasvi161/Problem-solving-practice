arr = [3, 2, 1, 5, 6, 4]
k = 2

unique = list(set(arr))

for i in range(k):
    largest = unique[0]

    for num in unique:
        if num > largest:
            largest = num

    if i == k - 1:
        print("Kth largest element:", largest)
    else:
        unique.remove(largest)