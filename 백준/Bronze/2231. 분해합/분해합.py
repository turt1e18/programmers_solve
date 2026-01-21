from sys import stdin

input = stdin.readline
n = int(input().rstrip())

for i in range(1,n+1):
    min_add = list(map(int,str(i)))
    result = i + sum(min_add)
    if n == result:
        print(i)
        break
    if n == i:
        print(0)
        break
