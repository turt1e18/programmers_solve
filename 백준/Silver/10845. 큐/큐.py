import sys

queue = []
count = 0

def push(data):
    global queue
    global count
    queue.append(data)
    count += 1

def pop():
    global queue
    global count
    if count == 0:
        print(-1)
        return
    print(queue[0])
    del queue[0]
    count -= 1

def size():
    global count
    print(count)

def empty():
    global count
    if count == 0:
        print(1)
    else:
        print(0)

def front():
    global queue
    global count
    if count == 0:
        print(-1)
        return
    print(queue[0])

def back():
    global queue
    global count
    if count == 0:
        print(-1)
        return
    print(queue[-1])

commandLine = int(sys.stdin.readline().rstrip())

for i in range(commandLine):
    cmdList = list(map(str, sys.stdin.readline().split()))
    if len(cmdList) > 1:
        if cmdList[0] == "push":
            push(int(cmdList[1]))
    else:
        if cmdList[0] == "pop":
            pop()
        elif cmdList[0] == "size":
            size()
        elif cmdList[0] == "empty":
            empty()
        elif cmdList[0] == "front":
            front()
        elif cmdList[0] == "back":
            back()