arr = [10, 20, 5, 20, 15, 10]

largest = second = float('-inf')

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

if second == float('-inf'):
    print("Second largest element does not exist")
else:
    print("Second largest unique element:", second)