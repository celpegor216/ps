from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
# 맨 오른쪽이 맨 위
lst_A = deque()
lst_B = deque()
for _ in range(N):
    a, b = map(int, input().split())
    lst_A.append(a)
    lst_B.append(b)


# lst_A, lst_B에서 가장 마지막으로 ground에 내려간 인덱스
ground_A = ground_B = N


def bell():
    global ground_A, ground_B, lst_A, lst_B

    if (ground_A < len(lst_A) and lst_A[ground_A] == 5) or (ground_B < len(lst_B) and lst_B[ground_B] == 5):
        move_B = len(lst_B) - ground_B
        move_A = len(lst_A) - ground_A
        for _ in range(move_B):
            lst_A.appendleft(lst_B.pop())
        for _ in range(move_A):
            lst_A.appendleft(lst_A.pop())
        ground_A = len(lst_A)
        ground_B = len(lst_B)
    elif ground_A < len(lst_A) and ground_B < len(lst_B) and lst_A[ground_A] + lst_B[ground_B] == 5:
        move_B = len(lst_B) - ground_B
        move_A = len(lst_A) - ground_A
        for _ in range(move_A):
            lst_B.appendleft(lst_A.pop())
        for _ in range(move_B):
            lst_B.appendleft(lst_B.pop())
        ground_A = len(lst_A)
        ground_B = len(lst_B)


for m in range(M):
    if not m % 2:
        ground_A -= 1
    else:
        ground_B -= 1
    
    if ground_A == 0:
        print('su')
        break
    elif ground_B == 0:
        print('do')
        break
    
    bell()
else:
    if ground_A > ground_B:
        print('do')
    elif ground_A < ground_B:
        print('su')
    else:
        print('dosu')