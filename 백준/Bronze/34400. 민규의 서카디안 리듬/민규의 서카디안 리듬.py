from sys import stdin

input = stdin.readline

count = int(input().rstrip())
for i in range(count):
    hour = int(input().rstrip())
    result = 0
    if hour >= 25:
        result = hour % 25 + 0.5
    else:
        result = hour + 0.5
    if result > 17 and result <= 24.5:
        print("OFFLINE")
    else:
        print("ONLINE")