from sys import stdin
from collections import deque

input = stdin.readline

lineCount = int(input().rstrip())
total = []
for i in range(lineCount):
    data = list(input().rstrip().split(" "))
    result = []
    for i in range(len(data)):
        result.append(data.pop())
    total.append(result)

for i in range(lineCount):
    print("Case #"+str(i+1)+": "+" ".join(total[i]))