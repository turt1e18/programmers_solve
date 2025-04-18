from sys import stdin

input = stdin.readline

data = list(map(int, input().rstrip().split(",")))
result = 0
for i in data:
    result += i

print(result)