string = "leetcode"
word_dict = ["leet", "code"]

dp = [False] * (len(string) + 1)
dp[0] = True

for i in range(1, len(string) + 1):
    for j in range(i):
        if dp[j] and string[j:i] in word_dict:
            dp[i] = True
            break

if dp[len(string)]:
    print("Word Break is possible")
else:
    print("Word Break is not possible")