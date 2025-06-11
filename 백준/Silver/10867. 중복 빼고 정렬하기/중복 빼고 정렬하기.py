from sys import stdin

input = stdin.readline

count = int(input().rstrip())
arr = list(set(map(int, input().rstrip().split(" "))))
sortArr = sorted(arr)
print(" ".join(map(str,sortArr)))