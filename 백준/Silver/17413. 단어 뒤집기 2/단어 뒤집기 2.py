from sys import stdin

input = stdin.readline
stack = []
stackmode = True

string = input().rstrip()
result = []

for i in string:
    if i == "<":
        while stack:
            result.append(stack.pop())
        result.append(i)
        stackmode = False

    elif i == ">":
        result.append(i)
        stackmode = True

    elif stackmode == False:
        result.append(i)

    elif i == " " and stackmode == True:
        while stack:
            result.append(stack.pop())
        result.append(i)
    elif stackmode == True:
        stack.append(i)

if len(stack) >= 1:
    while stack:
        result.append(stack.pop())


print("".join(result))