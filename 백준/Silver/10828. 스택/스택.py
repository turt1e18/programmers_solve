import sys

stack = []
count = 0

def push(data):
    global count
    global stack
    stack.append(data)
    count += 1

def pop():
    global count
    global stack
    if(count == 0):
        print(-1)
        return
    print(stack.pop())
    count -= 1

def top():
    global count
    global stack

    if(count == 0):
        print(-1)
        return
    print(stack[-1])

def size():
    global count
    print(count)

def empty():
    global count
    if(count == 0):
        print(1)
    else:
        print(0)

commandLine = int(sys.stdin.readline().rstrip())

for i in range(commandLine):
    cmdList = list(map(str,sys.stdin.readline().split()))
    if(len(cmdList) > 1):
        if(cmdList[0] == "push"):
            push(int(cmdList[1]))
        elif(cmdList[0] == "pop"):
            pop()
        elif(cmdList[0] == "top"):
            top()
        elif(cmdList[0] == "size"):
            size()
        elif(cmdList[0] == "empty"):
            empty()
    else:
        if(cmdList[0] == "pop"):
            pop()
        elif(cmdList[0] == "top"):
            top()
        elif(cmdList[0] == "size"):
            size()
        elif(cmdList[0] == "empty"):
            empty()