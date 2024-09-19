# 해답: https://77dptjd.tistory.com/55


import sys
input = sys.stdin.readline


N, M = map(int, input().split())
lst = list(map(int, input().split())) + [0]
result = 0

now = 0
for i in range(N):
    if lst[i]:
        if not now:
            now = 1
            result += 1
    else:
        now = 0


for _ in range(M):
    cmd = list(map(int, input().split()))

    if cmd[0] == 0:
        print(result)
    else:
        idx = cmd[1] - 1
        if lst[idx]:
            continue

        lst[idx] = 1

        # 오른쪽만 확인
        if idx == 0:
            if lst[idx + 1] == 0:
                result += 1
        # 왼쪽만 확인
        elif idx == N - 1:
            if lst[idx - 1] == 0:
                result += 1
        # 양쪽 다 확인
        else:
            if lst[idx + 1] == 0 and lst[idx - 1] == 0:
                result += 1
            elif lst[idx + 1] == 1 and lst[idx - 1] == 1:
                result -= 1