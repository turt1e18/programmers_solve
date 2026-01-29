from sys import stdin

input = stdin.readline

n = int(input().rstrip())
wight = []
for _ in range(n):
    wight.append(int(input().rstrip()))
wight.sort()

result = 0
for i in range(n):
    result = max(result,wight[i]*(n-i))

print(result)