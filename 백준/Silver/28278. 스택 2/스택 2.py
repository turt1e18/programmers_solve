from sys import stdin

input = stdin.readline
stack = []

command_line = int(input().rstrip())

for _ in range(command_line):
    command = list(input().rstrip().split(" "))
    if len(command) == 1:
        match command[0]:
            case "2":
                if len(stack) > 0:
                    print(stack.pop())
                else:
                    print(-1)
            case "3":
                print(len(stack))
            case "4":
                if len(stack) > 0:
                    print(0)
                else:
                    print(1)
            case "5":
                if len(stack) > 0:
                    print(stack[-1])
                else:
                    print(-1)
    else:
        stack.append(int(command[1]))