from sys import stdin
input = stdin.readline

ranked, myPoint, canRankCount = map(int, input().rstrip().split(" "))

# 0명있으면 1등이지
if ranked == 0: 
    print(1)
else:
    rankList = list(map(int, input().rstrip().split(" ")))
    # 랭킹이랑 랭킹가능 수랑 같은데 마지막 랭커가 내 점수보다 높거나 같으면 -1
    if ranked == canRankCount and rankList[ranked-1] >= myPoint:
        print(-1)
    else:
        for i in range(ranked):
            if rankList[i] <= myPoint:
                print(i + 1)
                break
        else:
            print(ranked + 1)
