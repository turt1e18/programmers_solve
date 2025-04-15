from sys import stdin

input = stdin.readline

while True:
    a, b = map(int, input().rstrip().split(" "))
    if a < 1 and b < 1: break
    else : print(a+b)
