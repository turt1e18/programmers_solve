from sys import stdin

listSize = int(stdin.readline().rstrip())
indexList = list(map(int, stdin.readline().split(" ")))
cmdline = int(stdin.readline().rstrip())

mistake = [0] * (listSize - 1)
for i in range(listSize - 1):
    if indexList[i] > indexList[i+1]:
        mistake[i] = 1

prefix = [0] * listSize
for i in range(1, listSize):
    prefix[i] = prefix[i - 1] + mistake[i - 1]

result = []
for _ in range(cmdline):
    x, y = map(int, stdin.readline().split(" "))
    result.append(str(prefix[y - 1] - prefix[x - 1]))

print("\n".join(result))