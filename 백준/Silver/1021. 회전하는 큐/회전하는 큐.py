from collections import deque
from sys import stdin
dqCommand = list(map(int,stdin.readline().split()))
delCase = list(map(int,stdin.readline().split()))

count = 0
dq = deque([i for i in range(1, dqCommand[0]+1)])

for i in delCase:
    while True:
        if(i == dq[0]):
            dq.popleft()
            break
        else:
            if dq.index(i) <= len(dq)//2:
                dq.rotate(-1)
                # print("rotate -1",dq)
                count += 1
            else:
                dq.rotate(1)
                # print("rotate 1",dq)
                count += 1 

print(count)


# 1. 입력 받을거 받기
# 2. 입력받은 길이로 deque 제작
# ==== delcase 만큼 ====
# 	3. del case 0번째 확인
# 	4. 해당 숫자가 어디에 있는지 파악 -> deque.index(data) = 해당 값의 index 리턴
# 	5 - 1. 길이의 절반이 보다 많으면 우측이동
# 	5 - 2. 길이의 절반보다 적으면 좌측이동
	