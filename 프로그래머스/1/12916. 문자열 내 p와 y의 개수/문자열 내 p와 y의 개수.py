def solution(s):
    answer = True
    countP = 0
    countY = 0
    a = list(s)
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(a)):
        if(a[i].upper() == "P"):
            countP += 1
        if(a[i].upper() == "Y"):
            countY += 1
    if(countP == countY):
        return True
    else:
        return False
