from sys import stdin

input = stdin.readline

countIngredient = int(input().rstrip())
armor = int(input().rstrip())
ingredient = list(map(int,input().split(" ")))
count = 0
front,back = 0,len(ingredient) - 1
ingredient = sorted(ingredient)


while(front != back):
    result = ingredient[front] + ingredient[back]
    if armor < result:
        back -= 1
    elif armor == result:
        count += 1
        front += 1
    elif armor > result:
        front += 1

print(count)