# 링크드리스트로 풀어보려고 했는데 시간 초과/메모리 초과
# 힌트: deque 사용, left, right


from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    S = input().strip()

    left = deque()    # 현재 커서 기준 왼쪽에 있는 글자들
    right = deque()    # 현재 커서 기준 오른쪽에 있는 글자들

    for s in S:
        if s == '-':
            if left:
                left.pop()
        elif s == '<':
            if left:
                right.appendleft(left.pop())
        elif s == '>':
            if right:
                left.append(right.popleft())
        else:
            left.append(s)
    
    print(''.join(left) + ''.join(right))