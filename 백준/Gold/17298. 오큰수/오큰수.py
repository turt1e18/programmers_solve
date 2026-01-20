from sys import stdin

input = stdin.readline
list_len = int(input().rstrip())

stack = []
result = ["-1"] * list_len

num_list = list(map(int, input().split(" ")))

for i in range(list_len):
    while stack and num_list[stack[-1]] < num_list[i]:
        id = stack.pop()
        result[id] = str(num_list[i])
    stack.append(i)

print(" ".join(result))
