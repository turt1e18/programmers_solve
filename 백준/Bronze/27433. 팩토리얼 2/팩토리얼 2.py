from sys import stdin

input = stdin.readline

n = int(input().rstrip())
a = 1

for i in range(1,n+1): a = a * i

print(a)
