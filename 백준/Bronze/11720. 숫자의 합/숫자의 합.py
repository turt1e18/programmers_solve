import sys

c = int(sys.stdin.readline().rstrip())
a = list(input())
b = 0
for i in a:
    b += int(i)
print(b)