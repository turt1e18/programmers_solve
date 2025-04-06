from sys import stdin

input = stdin.readline

maxNum = int(input().rstrip())
count = 0
for i in range(1, maxNum + 1):
    temp = list(str(i))
    if "3" in temp or "6" in temp or "9" in temp:
        a = temp.count("3")
        b = temp.count("6")
        c = temp.count("9")
        count = a + b + c + count
        
print(count)