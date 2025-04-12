from sys import stdin

input = stdin.readline

n, index = map(int, input().rstrip().split(" "))
divisor = []

for i in range(1, n+1):
    if n % i == 0:
        divisor.append(i)

if len(divisor) >= index: print(divisor[index-1])
else: print(0)