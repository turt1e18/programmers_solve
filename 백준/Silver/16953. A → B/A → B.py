from sys import stdin
from collections import deque

input = stdin.readline

start, end = map(int, input().rstrip().split(" "))
route = deque([(start, 1)])
while route:
    now, count = route.popleft()
    if now == end:
        print(count)
        exit()

    if now * 2 <= end: route.append((now*2,count+1))
    if now * 10 + 1 <= end: route.append((now*10+1, count+1)) 
print(-1)