from sys import stdin
from collections import deque
input = stdin.readline

n = int(input().rstrip())

dq = deque(range(1,n+1))
result = []

for i in range(n):
    if i == 0:
        result.append(str(dq.popleft()))
    else:
        dq.rotate(-1)
        result.append(str(dq.popleft()))

print(" ".join(result))