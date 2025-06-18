from sys import stdin
from collections import deque

input = stdin.readline

dq = deque()

count = int(input().rstrip())
operation = input().rstrip()
numList = [0] * count

for i in range(count):
    numList[i] = int(input().rstrip())


for i in operation:

    if "A" <= i <= "Z":
        dq.append(numList[ord(i) - ord("A")])
    else:
        temp2 = dq.pop()
        temp1 = dq.pop()
        if i == "+":
            dq.append(temp1 + temp2)
        elif i == "-":
            dq.append(temp1 - temp2)
        elif i == "*":
            dq.append(temp1 * temp2)
        elif i == "/":
            dq.append(temp1 / temp2)

print("%.2f" % dq[0])