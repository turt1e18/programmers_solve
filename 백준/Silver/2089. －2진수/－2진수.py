from sys import stdin

input = stdin.readline

num = int(input().rstrip())
result = ""
if num == 0:
    print(0)
    exit()

while num:
    if num % -2:
        num = num//-2 + 1
        result = "1" + result
    else:
        num = num//-2
        result = "0" + result

print(result)