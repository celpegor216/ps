# 시간 초과 해결 힌트: deque 사용
# 해답: https://velog.io/@j1min/Python-%EB%B0%B1%EC%A4%80-1406-%EC%97%90%EB%94%94%ED%84%B0-%ED%92%80%EC%9D%B4
from collections import deque
import sys

input = sys.stdin.readline

S = input().strip()
left = deque(S) # 커서 기준 왼쪽
right = deque() # 커서 기준 오른쪽

M = int(input())
for m in range(M):
    temp = input().strip()

    if temp[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif temp[0] == 'D':
        if right:
            left.append(right.popleft())
    elif temp[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(temp[-1])

print(''.join(left) + ''.join(right))