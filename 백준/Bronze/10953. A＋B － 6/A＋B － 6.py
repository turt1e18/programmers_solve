from sys import stdin

input = stdin.readline

cmdline = int(input().rstrip())
result = []

for _ in range(cmdline):
    a,b = map(int, input().rstrip().split(","))
    result.append(str(a+b))

print("\n".join(result))