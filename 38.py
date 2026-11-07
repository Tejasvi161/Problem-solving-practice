def permutations(arr):
    result = []
    arr.sort()

    def backtrack(path, used):
        if len(path) == len(arr):
            result.append(path.copy())
            return

        for i in range(len(arr)):
            if used[i]:
                continue

            # Skip duplicate elements
            if i > 0 and arr[i] == arr[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            path.append(arr[i])

            backtrack(path, used)

            path.pop()
            used[i] = False

    backtrack([], [False] * len(arr))
    return result


arr = ['A', 'A', 'B']

print("Permutations:")
for p in permutations(arr):
    print("".join(p))