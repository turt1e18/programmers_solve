from sys import stdin

input = stdin.readline

lost, brand = map(int, input().rstrip().split(" "))
setprice , oneprice = 0,0
result = 0

for _ in range(brand):
    bset, bone = map(int, input().rstrip().split(" "))
    
    if setprice == 0 and oneprice == 0:
        setprice = bset
        oneprice = bone

    if bset < setprice:
        setprice = bset
    if bone < oneprice:
        oneprice = bone

if lost <= 6:
    if setprice < oneprice * lost:
        result = setprice
    else:
        result = oneprice * lost
else:
    index = 0
    afterLost = 0
    if lost % 6 != 0:
        afterLost = lost % 6
        index = lost // 6
    else:
        index = lost // 6

    if setprice <= oneprice:
        if afterLost > 0:
            result = setprice * (index+1)
        else:
            result = setprice * index
        # print("세트 가격이 개당 가격 이하일때", setprice * index)

    else:
        onlyset = 0
        if afterLost > 0:
            onlyset = setprice * (index+1)
        else:
            onlyset = setprice * index
        onlyone = oneprice * lost
        mixprice = setprice * index + oneprice * afterLost
        # print(onlyone, onlyset, mixprice)
        result = min(onlyone, onlyset, mixprice)
        
print(result)