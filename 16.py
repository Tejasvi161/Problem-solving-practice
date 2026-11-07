string = "{[()]}"
stack = []

for char in string:
    if char in "({[":
        stack.append(char)

    elif char in ")}]":
        if not stack:
            print("Not Balanced")
            break

        top = stack.pop()

        if (char == ')' and top != '(') or \
           (char == '}' and top != '{') or \
           (char == ']' and top != '['):
            print("Not Balanced")
            break
else:
    if not stack:
        print("Balanced")
    else:
        print("Not Balanced")