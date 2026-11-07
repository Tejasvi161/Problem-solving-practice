arr = ["flower", "flow", "flight"]

prefix = arr[0]

for word in arr[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

print("Longest common prefix:", prefix)