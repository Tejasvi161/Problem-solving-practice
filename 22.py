arr1 = [1, 3]
arr2 = [2]

if len(arr1) > len(arr2):
    arr1, arr2 = arr2, arr1

m = len(arr1)
n = len(arr2)

low = 0
high = m

while low <= high:
    i = (low + high) // 2
    j = (m + n + 1) // 2 - i

    left1 = float('-inf') if i == 0 else arr1[i - 1]
    right1 = float('inf') if i == m else arr1[i]

    left2 = float('-inf') if j == 0 else arr2[j - 1]
    right2 = float('inf') if j == n else arr2[j]

    if left1 <= right2 and left2 <= right1:
        if (m + n) % 2 == 0:
            median = (max(left1, left2) + min(right1, right2)) / 2
        else:
            median = max(left1, left2)

        print("Median:", median)
        break

    elif left1 > right2:
        high = i - 1
    else:
        low = i + 1