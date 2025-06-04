from sys import stdin

input = stdin.readline

n = int(input().rstrip())
result = 1
if n == 0:
    print(1)
else:
    for i in range(n):
        result *= i+1
    print(result) 