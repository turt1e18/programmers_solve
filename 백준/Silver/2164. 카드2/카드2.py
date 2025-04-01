from sys import stdin, stdout
from collections import deque

n = int(stdin.readline().rstrip())
queue = deque(range(1, n+1))
while len(queue) != 1:
    queue.popleft()
    queue.append(queue[0])
    queue.popleft()

stdout.write(str(queue[0]))
