from sys import stdin

input = stdin.readline

while True:
    try:
        a, b = map(int, input().rstrip().split(" "))
        print(a+b)
    except:
        break