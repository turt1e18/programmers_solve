from sys import stdin
input = stdin.readline

problemCount = int(input().rstrip())
pointList = list(map(int, input().rstrip().split(" ")))
stack = 0
count = 0
for i in range(problemCount):
    if pointList[i] == 1:
        stack += 1
        count += stack
    else:    
        stack = 0
print(count)