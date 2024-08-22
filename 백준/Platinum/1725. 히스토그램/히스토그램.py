import sys
input = sys.stdin.readline

N = int(input())

stack = []
result = 0

for n in range(N):
    num = int(input())
    idx = n

    while stack and stack[-1][1] > num:
        result = max(result, stack[-1][1] * (n - stack[-1][0]))
        idx = stack[-1][0]
        stack.pop()

    stack.append((idx, num))

while stack:
    result = max(result, stack[-1][1] * (N - stack[-1][0]))
    stack.pop()

print(result)