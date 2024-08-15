from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

q = deque()
result = []

for _ in range(N):
    command = list(map(int, input().split()))

    if command[0] == 1:
        q.appendleft(command[1])
    elif command[0] == 2:
        q.append(command[1])
    elif command[0] == 3:
        result.append(q.popleft() if q else -1)
    elif command[0] == 4:
        result.append(q.pop() if q else -1)
    elif command[0] == 5:
        result.append(len(q))
    elif command[0] == 6:
        result.append(0 if q else 1)
    elif command[0] == 7:
        result.append(q[0] if q else -1)
    elif command[0] == 8:
        result.append(q[-1] if q else -1)

for item in result:
    print(item)