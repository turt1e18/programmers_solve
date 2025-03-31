from sys import stdin

result = []

while True:
    stack = []
    inputList = list(stdin.readline().rstrip())
    if len(inputList) == 1 and inputList[0] == ".":
        break
    for i in inputList:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")" or i == "]":
            if len(stack) == 0 and (i == ")" or i == "]"):
                stack.append("end")
                break
            if i == ")" and stack[-1] == "(":
                stack.pop()
            elif i == "]" and stack[-1] == "[":
                stack.pop()
            elif i == ")" and stack[-1] == "[":
                stack.append("end")
                break
            elif i == "]" and stack[-1] == "(":
                stack.append("end")
                break
        # print(i,", ",stack)
        
    if len(stack) == 0:
        result.append("yes")
    else:
        result.append("no")

for i in result: print(i)