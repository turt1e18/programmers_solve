from sys import stdin
input = stdin.readline

n = int(input().rstrip())
prev, now=0,1

for _ in range(n):
    prev, now = now, prev+now
print(prev)