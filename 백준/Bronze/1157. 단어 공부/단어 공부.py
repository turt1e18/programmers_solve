from sys import stdin
from collections import Counter
input = stdin.readline

word = list(input().upper().rstrip())
counter = Counter(word)


# if len(word) < 2:
#     resultSample = counter.most_common(1)
#     print(resultSample[0][0])
# else:
#     resultSample = counter.most_common(2)

#     if resultSample[0][1] == resultSample[1][1]: print("?")
#     else: print(resultSample[0][0])

resultSample = counter.most_common(2)

if len(resultSample) == 1:
    print(resultSample[0][0])
elif resultSample[0][1] == resultSample[1][1]:
    print("?")
else:
    print(resultSample[0][0])