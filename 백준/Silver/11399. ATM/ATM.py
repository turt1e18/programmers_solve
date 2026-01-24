from sys import stdin

input = stdin.readline

people = int(input().rstrip())
time = list(map(int,input().rstrip().split(" ")))

result,temp = 0,0
time.sort()

for i in time:
    temp += i 
    result += temp

print(result)