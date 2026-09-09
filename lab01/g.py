s = input()

stack = []

for letter in s:
    if stack and stack[-1] == letter:
        stack.pop()
    else:
        stack.append(letter)

if not stack:
    print("YES")
else:
    print("NO")
