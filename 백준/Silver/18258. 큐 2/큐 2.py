from sys import stdin
from collections import deque

input = stdin.readline
cmdLine = int(input().rstrip())

dq = deque()

def push(data):
    global dq
    dq.append(int(data))

def pop():
    global dq
    if len(dq) < 1:
        print(-1)
        return
    print(dq.popleft())

def empty():
    global dq
    if len(dq) < 1:
        print(1)
    else: print(0)

def size():
    global dq
    print(len(dq))

def front():
    global dq
    if len(dq) < 1:
        print(-1)
        return
    
    print(dq[0])

def back():
    global dq
    if len(dq) < 1:
        print(-1)
        return
    
    print(dq[-1])

for _ in range(cmdLine):
    cmd = list(map(str,input().rstrip().split(" ")))
    # print(cmd)
    if len(cmd) > 1:
        push(cmd[1])
    else:
        if cmd[0] == "front":
            front()
        elif cmd[0] == "back":
            back()
        elif cmd[0] == "size":
            size()
        elif cmd[0] == "empty":
            empty()
        elif cmd[0] == "pop":
            pop()