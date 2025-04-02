from sys import stdin
from collections import deque

cmdList = int(stdin.readline().rstrip())
result = []

for _ in range(cmdList):
    isError = False
    isReverse = False

    cmd = stdin.readline().rstrip()
    n = int(stdin.readline().rstrip())
    arr = stdin.readline().strip()

    # 빈 배열 처리
    if n == 0:
        dq = deque()
    else:
        listArr = list(map(int, arr.strip()[1:-1].split(",")))
        dq = deque(listArr)

    for c in cmd:
        if c == "R":
            isReverse = not isReverse
        else:
            if not dq:
                isError = True
                break
            # 뒤집기 여부에 따라 pop 또는 popleft
            if isReverse:
                dq.pop()
            else:
                dq.popleft()

    if isError:
        result.append("error")
    else:
        # 뒤집힌 상태에 따라 덱을 리스트로 변환
        if isReverse:
            dq.reverse()
        result.append(f"[{','.join(map(str, dq))}]")

# 한 번에 출력하여 시간 초과 방지
print("\n".join(result))
