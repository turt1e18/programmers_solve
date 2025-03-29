from sys import stdin

cmdCase = int(stdin.readline().rstrip())
result = [] * cmdCase

for i in range(cmdCase):
    caseList = list(input())
    stackList = []
    
    if caseList[0] == ")":
        result.append("NO")
        continue
    
    for j in caseList: 
        
        if j == '(':
            stackList.append(0)
        elif j == ')':
            if len(stackList) == 0:
                 stackList.append(1)
                 break
            else:
                stackList.pop()
    
    if len(stackList) != 0:
        result.append("NO")
    else:
        result.append("YES")

for i in result: print(i)