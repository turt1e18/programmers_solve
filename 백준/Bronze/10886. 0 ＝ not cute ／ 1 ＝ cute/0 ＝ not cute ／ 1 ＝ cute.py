from sys import stdin

cmdLine = int(stdin.readline().rstrip())
arr = [0] * 2
for _ in range(cmdLine):
    num = int(stdin.readline().rstrip())
    if num == 1: arr[1] += 1
    elif num == 0: arr[0] += 1
if arr[0] < arr[1]: print("Junhee is cute!")
else: print("Junhee is not cute!")