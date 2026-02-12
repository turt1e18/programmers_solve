from sys import stdin

inpuut = stdin.readline

n = int(input().rstrip())

stack = [0,1]

for i in range(n):
    stack.append(stack[i]+stack[i+1])

print(stack[n])