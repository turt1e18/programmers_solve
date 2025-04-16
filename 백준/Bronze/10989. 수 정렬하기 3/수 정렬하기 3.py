import sys

count = int(sys.stdin.readline().rstrip())
a = [0] * 10001
index = 0

for _ in range(count):
    num = int(sys.stdin.readline().rstrip())
    a[num] += 1



for i in range(1, 10001):
    if(a[i] != 0): 
        for _ in range(a[i]):
            print(i)