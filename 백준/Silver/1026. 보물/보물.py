from sys import stdin

input = stdin.readline

n = int(input().rstrip())
a = list(map(int, input().rstrip().split(" ")))
b = list(map(int, input().rstrip().split(" ")))

a.sort()

result = 0
for i in range(n):
    result += a[i] * max(b)
    b[b.index(max(b))] = -1

print(result)
