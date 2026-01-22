from sys import stdin

input = stdin.readline

candy_set = int(input().rstrip())
candy_list = list(map(int, input().rstrip().split(" ")))
candy_list.sort()
result = 0

even = list(filter(lambda x: x%2 == 0, candy_list))
odd = list(filter(lambda x: x%2 != 0, candy_list))

if len(odd) % 2 == 0:
    result += sum(odd)
else:
    for i in range(len(odd)-1, 0, -1):
        if i == 0:
            break
        result += odd[i]

result += sum(even)

if result % 2 == 0:
    print(result)
else:
    print(0)