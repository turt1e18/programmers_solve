import sys

cmdCount = int(sys.stdin.readline().rstrip())
deque = []
count = 0

def push_front(data):
    global deque
    global count
    deque.insert(0,data)
    count += 1

def push_back(data):
    global deque
    global count
    deque.append(data)
    count += 1

def pop_front():
    global deque
    global count
    if(count == 0):
        print(-1)
        return
    print(deque[0])
    del deque[0]
    count -= 1

def pop_back():
    global deque
    global count
    if(count == 0):
        print(-1)
        return
    print(deque.pop())
    count -= 1

def size():
    global count
    print(count)

def empty():
    global count
    if(count == 0):
        print(1)
    else:
        print(0)

def front():
    global deque
    global count
    if(count == 0):
        print(-1)
        return
    print(deque[0])

def back():
    global deque
    global count
    if(count == 0):
        print(-1)
        return
    print(deque[-1])


for i in range(cmdCount):
    cmdList = list(map(str,sys.stdin.readline().split()))
    if len(cmdList) > 1:
        if cmdList[0] == "push_front":
            push_front(cmdList[1])
        elif cmdList[0] == "push_back":
            push_back(cmdList[1])
    else:
        if cmdList[0] == "pop_front":
            pop_front()
        elif cmdList[0] == "pop_back":
            pop_back()
        elif cmdList[0] == "size":
            size()
        elif cmdList[0] == "empty":
            empty()
        elif cmdList[0] == "front":
            front()
        elif cmdList[0] == "back":
            back()