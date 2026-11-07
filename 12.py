string = "abcabcbb"

longest = ""

for i in range(len(string)):
    current = ""

    for j in range(i, len(string)):
        if string[j] not in current:
            current += string[j]
        else:
            break

    if len(current) > len(longest):
        longest = current

print("Longest substring:", longest)
print("Length:", len(longest))