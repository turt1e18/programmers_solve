from sys import stdin
from collections import deque
input = stdin.readline

node,line,start = map(int, input().rstrip().split(" "))

def dfs(graph, now, visitList):
    visitList[now] = True
    print(now, end=" ")
    for i in graph[now]:
        if not visitList[i]:
            dfs(graph,i,visitList)

def bfs(graph, now, visitList):
    dq = deque([now])
    visitList[now] = True
    while dq:
        v = dq.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visitList[i]:
                dq.append(i)
                visitList[i] = True



graph = [[] for _ in range(node + 1)]
isVisited = [False] * (node + 1)

for _ in range(line):
    n, m = map(int, input().rstrip().split(" "))
    graph[n].append(m)
    graph[m].append(n)

for i in graph:
    i.sort()

# print(graph)
dfs(graph,start,isVisited)

isVisitedBfs = [False] * (node+1)
print()
bfs(graph,start,isVisitedBfs)