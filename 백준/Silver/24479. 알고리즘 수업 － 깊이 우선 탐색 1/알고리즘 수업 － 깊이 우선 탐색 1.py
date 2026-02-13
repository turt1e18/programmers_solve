from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

input = stdin.readline

n,l,s = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
line = [0] * (n+1)
count = 1

for _ in range(l):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1,n+1):
    graph[i].sort()

def dfs(node):
    global count
    visited[node] = True
    line[node] = count
    count += 1

    for i in graph[node]:
        if not visited[i]:
            dfs(i)

dfs(s)

for i in range(1,len(line)):
    print(line[i])