from sys import stdin

input = stdin.readline

a,b = map(int, input().split(" "))
numList = list(map(int, input().split(" ")))
result = []
for i in numList:
    if i < b:
        result.append(str(i))

print(" ".join(result))