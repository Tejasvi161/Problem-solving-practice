str1 = "listen"
str2 = "silent"

if len(str1) == len(str2):
    for char in str1:
        if str1.count(char) != str2.count(char):
            print("Not Anagrams")
            break
    else:
        print("Anagrams")
else:
    print("Not Anagrams")