arr = [10, 9, 2, 5, 3, 7, 101, 18]

dp = [1] * len(arr)
previous = [-1] * len(arr)

for i in range(len(arr)):
    for j in range(i):
        if arr[i] > arr[j] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            previous[i] = j

index = dp.index(max(dp))
result = []

while index != -1:
    result.append(arr[index])
    index = previous[index]

result.reverse()

print("Longest increasing subsequence:", result)
print("Length:", len(result))