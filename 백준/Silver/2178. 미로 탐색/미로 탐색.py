from sys import stdin
from collections import deque

input = stdin.readline

n,m = map(int, input().rstrip().split())

# 하상
wayy = [0,0,1,-1]
# 우좌
wayx = [1,-1,0,0]
route = [[0]*m for _ in range(n)]

labyrinth = []
for i in range(n):
    labyrinth.append(list(map(str,input().rstrip())))

d = deque([(0,0)])
route[0][0] = 1

while d:
    x, y = d.popleft()

    for i in range(4):
        nx = x + wayx[i]
        ny = y + wayy[i]

        if nx < 0 or ny >= n or ny< 0 or nx >= m:
            continue
        if labyrinth[ny][nx] == "0":
            continue
        if route[ny][nx] != 0:
            continue

        route[ny][nx] = route[y][x]+1
        d.append((nx,ny))

print(route[n-1][m-1])
