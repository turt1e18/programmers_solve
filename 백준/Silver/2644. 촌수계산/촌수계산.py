from sys import stdin
from collections import deque

input = stdin.readline

p = int(input().rstrip())
s, e = map(int,input().split())
line = int(input().rstrip())

f_tree = [[] for _ in range(p+1)]
visited = [False] * (p+1)
count = 0

def dfs(node, cnt):
    visited[node] = True
    if node == e:
        return cnt
    
    for i in f_tree[node]:
        if not visited[i]:
            r = dfs(i,cnt+1)
            if r != -1:
                return r
    return -1

for _ in range(line):
    parent, child = map(int,input().split())
    f_tree[parent].append(child)
    f_tree[child].append(parent)

print(dfs(s,count))