from sys import stdin

input = stdin.readline

node = int(input().rstrip())
cmdLine = int(input().rstrip())

gragh = [[ ] for _ in range(node + 1)]
path = [False] * (node + 1)


def dfs(now, pathList):
    pathList[now] = True
    # print(now, end=" ")
    for i in gragh[now]:
        if not pathList[i]:
            dfs(i, pathList)

for _ in range(cmdLine):
    n, m = map(int, input().rstrip().split())
    gragh[n].append(m)
    gragh[m].append(n)

for i in gragh:
    i.sort()

dfs(1, path)

print(path.count(True)-1)