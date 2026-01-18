from sys import stdin

input = stdin.readline

multitab = int(input().rstrip())
sum = 0
for i in range(multitab):
    sum += int(input().rstrip())

print(sum - (multitab - 1))