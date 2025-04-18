from sys import stdin

input = stdin.readline

n = int(input().rstrip())
result = []
for _ in range(n):
    string = list(input().rstrip())
    result.append(string[0]+string[-1])

print("\n".join(result))