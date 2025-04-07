from sys import stdin
from collections import deque
input = stdin.readline

cmdList = list(map(int,input().split(" ")))

# print(cmdList)
dq = deque(range(1, cmdList[0]+1))
newList = []

for _ in range(cmdList[0] - 1):
    dq.rotate(-(cmdList[1]-1))
    newList.append(str(dq.popleft()))
newList.append(str(dq.pop()))
# print(newList)
print("<"+", ".join(newList)+">")