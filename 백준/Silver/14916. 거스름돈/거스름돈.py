from sys import stdin

input = stdin.readline

n = int(input().rstrip())
count = 0

five = n // 5

while n != 0:
    if five == 0 and n % 2 != 0:
        count = -1
        break
    if (n - 5 * five) % 2 == 0:
        count = five + ((n - 5 * five) // 2)
        break
    else: 
        five -= 1
    
print(count)