from sys import stdin

input = stdin.readline

count = int(input().rstrip())
p_list = []

for i in range(count):
    age, name = input().split()
    p_list.append((int(age),i,name))

p_list.sort(key=lambda x: (x[0],x[1]))

for age, _, name in p_list:
    print(age, name)