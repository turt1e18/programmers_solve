import sys

a,b = map(int,sys.stdin.readline().split())
line = 1
numList = []

while len(numList) < b:
    for j in range(line):
        if len(numList) > b: break
        numList.append(line)
    line += 1

result = 0

for i in range(a - 1,b ):
    result += numList[i]

print(result)