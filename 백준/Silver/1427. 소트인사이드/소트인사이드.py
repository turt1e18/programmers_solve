from sys import stdin

input = stdin.readline

strList = list(map(int,input().rstrip()))

a = list(map(str,reversed(sorted(strList))))

print("".join(a))