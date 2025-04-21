from sys import stdin
from collections import deque

input = stdin.readline

cmdline = int(input().rstrip())
result = []

for _ in range(cmdline):
    count = 0
    maxValue = 0
    n, m = map(int, input().rstrip().split(" "))
    data = list(enumerate(map(int,input().rstrip().split(" ")))) 
    dq = deque(data)

    while True:
        # print(dq)
        if max(dq, key=lambda x: x[1])[1] == dq[0][1]:
            # print(max(dq, key=lambda x: x[1])[1], dq[0][1])

            temp = dq.popleft()
            count += 1
            if m == temp[0]:
                result.append(str(count))
                break
        else:
            dq.rotate(-1)
    
print(" ".join(result))