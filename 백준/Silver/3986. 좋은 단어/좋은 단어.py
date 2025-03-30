from sys import stdin

cmdLine = int(stdin.readline().rstrip())
resultStack = 0

for i in range(cmdLine):
    stack = []
    aType = 0
    bType = 0

    inputData = list(stdin.readline().rstrip())
    
    for j in inputData:
        if len(stack) != 0 and stack[-1] == j:
            if j == "A":
                aType += 1
            else:
                bType += 1
            stack.pop()
        else:    
            if j == "A":
                aType += 1
            else:
                bType += 1
            stack.append(j)
    if len(stack) == 0:
        resultStack += 1
    # print(stack)
print(resultStack)