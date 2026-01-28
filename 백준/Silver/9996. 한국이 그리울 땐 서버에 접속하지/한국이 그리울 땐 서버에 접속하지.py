from sys import stdin

input = stdin.readline

line = int(input().rstrip())
pattern_start, pattern_end = map(str,input().rstrip().split("*"))
for _ in range(line):
    data = list(input().rstrip())
    count = False
    if len(data) < len(pattern_start + pattern_end):
        print("NE")
        continue

    
    count = True
    
    for i in range(len(pattern_start)):
        if pattern_start[i] != data[i]:
            count = False
            break

    for i in range(1, len(pattern_end)+1):
        if pattern_end[-i] != data[-i]:
            count = False
            break
        
    if not count: print("NE")
    else: print("DA")