from sys import stdin

input = stdin.readline

n = int(input().rstrip())

for _ in range(n):
    facto = int(input().rstrip())
    count = 0
    
    while facto >= 5:
        facto //= 5
        count += facto
    print(count)