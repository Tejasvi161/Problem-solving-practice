arr = [1, 2, 3, 4, 2, 1]
target = 6

for i in range(len(arr)):
    current_sum = 0

    for j in range(i, len(arr)):
        current_sum += arr[j]

        if current_sum == target:
            print(arr[i:j+1])