from sys import stdin

input = stdin.readline
alpha = [0] * 26
data = list(input().rstrip())

isOdd = 0

for i in data:
    alpha[ord(i)-65] += 1

for i in alpha:
    if i % 2 != 0:
        isOdd += 1
        if isOdd > 1:
            print("I'm Sorry Hansoo")
            exit()
front = []
mid = ""
back = ""

for i in range(26):
    front.append(chr(i+65) * (alpha[i] // 2))
    if alpha[i] % 2 != 0:
        mid = chr(i+65)

back = "".join(front)[::-1]

print("".join(front)+mid+back)