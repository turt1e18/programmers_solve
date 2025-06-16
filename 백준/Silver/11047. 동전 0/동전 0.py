from sys import stdin
input = stdin.readline

count, change = map(int, input().rstrip().split(" "))
typeCoin = []
result = 0

for i in range(count):
    typeCoin.append(int(input().rstrip()))

for i in range(count - 1, -1 ,-1):
    if typeCoin[i] <= change:
        result += (change // typeCoin[i])
        change = change % typeCoin[i]
print(result)