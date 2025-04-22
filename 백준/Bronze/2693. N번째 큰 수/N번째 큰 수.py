from sys import stdin

input = stdin.readline

time = int(input().rstrip())
result = []
for _ in range(time):
    # data = sorted(list(map(int, input().rstrip().split(" "))))
    result.append(str(sorted(list(map(int, input().rstrip().split(" "))))[-3]))

print("\n".join(result))