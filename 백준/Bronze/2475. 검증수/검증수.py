from sys import stdin

input = stdin.readline

data = list(map(int,input().rstrip().split(" ")))

before = 0

for i in data:
    before = i*i + before
before %= 10
print(before)