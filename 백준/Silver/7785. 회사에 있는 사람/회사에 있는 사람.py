from sys import stdin

input = stdin.readline

count = int(input().rstrip())
p_set = set()

for i in range(count):
    name,isIn = input().split()
    if isIn == "enter":
        p_set.add(name)
    elif isIn == "leave":
        p_set.discard(name)

p_set = sorted(p_set, reverse=True)
print("\n".join(p_set))