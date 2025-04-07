from sys import stdin

input = stdin.readline

cmdline = int(input())
result = []
for _ in range(cmdline):
    a, b = map(int, input().split(" "))
    result.append(a+b)

for i in result:
    print(i)