from sys import stdin

input = stdin.readline

a = list(map(int,input().rstrip().split("/")))
if a[1] < 1:
    print("hasu")
elif a[0] + a[2] < a[1]:
    print("hasu")
else:
    print("gosu")