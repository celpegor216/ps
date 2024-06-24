# 해답: https://welog.tistory.com/435

from collections import deque

A = sorted(input())
B = sorted(input())
N = len(A)

A = deque(A[:(N + 1) // 2])
B = deque(B[N - (N // 2):])

result = [''] * N

start, end = 0, N - 1

for n in range(N):
    if not n % 2:
        if B and A[0] < B[-1]:
            result[start] = A.popleft()
            start += 1
        else:
            result[end] = A.pop()
            end -= 1
    else:
        if A and A[0] < B[-1]:
            result[start] = B.pop()
            start += 1
        else:
            result[end] = B.popleft()
            end -= 1

print(''.join(result))