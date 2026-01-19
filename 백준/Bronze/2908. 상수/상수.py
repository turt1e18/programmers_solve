from sys import stdin

input = stdin.readline

a,b = map(int, input().rstrip().split(" "))
if int(str(a)[::-1]) > int(str(b)[::-1]):
    print(int(str(a)[::-1]))
else:
    print(int(str(b)[::-1]))