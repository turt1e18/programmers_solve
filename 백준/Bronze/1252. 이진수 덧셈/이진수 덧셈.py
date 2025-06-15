from sys import stdin
input = stdin.readline

binn = list(map(str, input().rstrip().split(" ")))
result = list(str(bin(int(binn[0],2)+int(binn[1],2))))
del result[0]
del result[0]

print("".join(result))