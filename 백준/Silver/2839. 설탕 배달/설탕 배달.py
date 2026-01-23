from sys import stdin

input = stdin.readline

suger = int(input().rstrip())

five = suger // 5

while True:
    if five == 0 and suger % 3 != 0:
        print(-1)
        break
    if (suger - 5 * five) % 3 == 0:
        print(five + (suger - 5 * five) // 3)
        break
    five -= 1
