from sys import stdin

input = stdin.readline

cmdLine = int(input().rstrip())
cow = [0] * 11
isMove = [None] * 11

for _ in range(cmdLine):
    cowNum, way = map(int, input().rstrip().split(" "))
    if isMove[cowNum] is None :
        isMove[cowNum] = way
        # print(cowNum, way, "변화!")
    elif isMove[cowNum] != way:
        isMove[cowNum] = way
        cow[cowNum] += 1
        # print("길건넘")
    else:
        pass

# print(isMove)
# print(cow)
result = 0
for i in cow:
    result += i
print(result)
