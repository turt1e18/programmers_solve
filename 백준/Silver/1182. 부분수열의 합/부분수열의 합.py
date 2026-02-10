from sys import stdin

input = stdin.readline
stack = [(0,0)]

n,s = map(int, input().split())
num = list(map(int,input().split()))
count = 0

while stack:
    index, total = stack.pop()
    if index == n:
        if total == s:
            count += 1
        continue
    stack.append((index+1,total+num[index]))
    stack.append((index+1,total))
if s == 0:
    count -= 1

print(count)