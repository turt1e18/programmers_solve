from sys import stdin
from collections import deque

input = stdin.readline

n, k = map(int, input().rstrip().split(" "))
dq = deque(range(1, n+1))

result = []
while len(dq) > 0:
    dq.rotate(-(k - 1))
#    print(dq)
    result.append(str(dq.popleft()))


print("<"+", ".join(result)+">")