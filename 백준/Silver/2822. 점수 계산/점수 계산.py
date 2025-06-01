from sys import stdin

input = stdin.readline

numbers = []
for i in range(8):
    numbers.append(int(input().rstrip()))

sortedList = list(reversed(sorted(numbers)))
result = 0
resultIndex = []

for i in range(len(numbers)):
    if i < 5: 
        result += sortedList[i]
        resultIndex.append(str(numbers.index(sortedList[i])+1))
    else: break 

print(result)
print(' '.join(sorted(resultIndex)))