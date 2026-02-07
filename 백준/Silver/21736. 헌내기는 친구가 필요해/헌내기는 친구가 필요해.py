from sys import stdin
input = stdin.readline

line, index = map(int, input().split())

commap = [list(input().rstrip()) for _ in range(line)]

visited = [[False]*index for _ in range(line)]
count = 0
dr = [1,-1,0,0]
dc = [0,0,1,-1]

for r in range(line):
    for c in range(index):
        if commap[r][c] == 'I':
            start_r, start_c = r, c


stack = [(start_r, start_c)]
visited[start_r][start_c] = True
count = 0

while stack:
    r, c = stack.pop()

    if commap[r][c] == 'P':
        count += 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= line or nc < 0 or nc >= index:
            continue
        if visited[nr][nc]:
            continue
        if commap[nr][nc] == 'X':
            continue

        visited[nr][nc] = True
        stack.append((nr, nc))

print(count if count > 0 else "TT")
