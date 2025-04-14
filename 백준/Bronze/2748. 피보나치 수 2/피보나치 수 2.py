from sys import stdin

input = stdin.readline

n = int(input().rstrip())
temp, temp2 = 0, 1
fibo = [0, 1]
for _ in range(n - 1):
    result = temp + temp2
    fibo.append(result)
    temp = temp2
    temp2 = result

print(fibo[-1])