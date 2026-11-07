arr1 = [1, 2, 2, 3, 4, 2]
arr2 = [2, 2, 4, 5]

result = []

for num in arr1:
    if num in arr2:
        result.append(num)
        arr2.remove(num)

print("Intersection:", result)
