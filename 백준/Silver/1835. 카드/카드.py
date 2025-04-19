from sys import stdin
from collections import deque

input = stdin.readline
n = int(input().rstrip())

dq = deque(range(n))
result = [0] * n

for i in range(n):
    temp = 0
    dq.rotate(-(i+1))
    # print(dq, i)
    result[dq.popleft()] = str(i+1)

print(" ".join(result))