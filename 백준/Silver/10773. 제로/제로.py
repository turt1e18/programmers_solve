import sys

cmdLine = int(sys.stdin.readline().rstrip())
stack = []

for i in range(cmdLine):
    command = int(sys.stdin.readline().rstrip())

    if(command == 0):
        stack.pop()
    else:
        stack.append(command)

b = 0

for i in stack:
    b += i

print(b)