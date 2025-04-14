from sys import stdin

input = stdin.readline

n = int(input().rstrip())
fibo = [0, 1]
for i in range(1, n):
    fibo.append(fibo[i - 1]+fibo[i])
print(fibo[-1])