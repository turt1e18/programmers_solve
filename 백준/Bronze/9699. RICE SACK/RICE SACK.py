from sys import stdin

input = stdin.readline

cmdline = int(input().rstrip())
result = []
for _ in range(cmdline):
    data = list(map(int, input().rstrip().split(" ")))
    result.append(max(data))

for i in range(len(result)):
    print("Case #"+str(i+1)+": "+str(result[i]))