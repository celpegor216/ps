from collections import deque
import sys
input = sys.stdin.readline


q = deque()
# 지금 큐가 가로인가?
is_horizontal = 1
# 지금 큐의 앞이 q의 오른쪽인가?
is_head_last = 1

cnts = [0] * 2

for _ in range(int(input())):
    cmd = input().strip()

    if cmd == 'push b':
        if is_horizontal or (is_head_last and cnts[1]):
            q.appendleft(0)
            cnts[0] += 1
    elif cmd == 'push w':
        q.appendleft(1)
        cnts[1] += 1
    elif cmd == 'pop':
        if q:
            cnts[q.pop()] -= 1

            # 앞이 아래인 세로 상태에서 가림막이 빠지면 그 위에 있던 공들 다 없애기
            if not is_horizontal and is_head_last:
                while q and q[-1] != 1:
                    cnts[q.pop()] -= 1
    elif cmd == 'rotate l':
        if is_horizontal:
            is_head_last = 1 - is_head_last
        is_horizontal = 1 - is_horizontal

        if not is_horizontal:
            if is_head_last:
                while q and q[-1] != 1:
                    cnts[q.pop()] -= 1
            else:
                while q and q[0] != 1:
                    cnts[q.popleft()] -= 1
    elif cmd == 'rotate r':
        if not is_horizontal:
            is_head_last = 1 - is_head_last
        is_horizontal = 1 - is_horizontal
        
        if not is_horizontal:
            if is_head_last:
                while q and q[-1] != 1:
                    cnts[q.pop()] -= 1
            else:
                while q and q[0] != 1:
                    cnts[q.popleft()] -= 1
    elif cmd == 'count b':
        print(cnts[0])
    elif cmd == 'count w':
        print(cnts[1])