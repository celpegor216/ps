from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

q = deque()

for n in range(N):
    temp = input().strip()

    if '0' <= temp[-1] <= '9':
        command, num = temp.split()

        q.append(int(num))
    else:
        if temp == 'pop':
            if not q:
                print(-1)
            else:
                print(q.popleft())
        elif temp == 'size':
            print(len(q))
        elif temp == 'empty':
            print(1 if not q else 0)
        elif temp == 'front':
            if not q:
                print(-1)
            else:
                print(q[0])
        else:
            if not q:
                print(-1)
            else:
                print(q[-1])