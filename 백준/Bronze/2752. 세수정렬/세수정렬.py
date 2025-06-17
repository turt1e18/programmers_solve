from sys import stdin
input = stdin.readline

sertList = list(map(int, input().rstrip().split(" ")))
result = list(map(str,sorted(sertList)))

print(" ".join(result))