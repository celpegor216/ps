import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort()

result = 0
stack = []
for n in range(N):
    if stack and stack[-1][1] < lst[n][0]:
        result += stack[-1][1] - stack[0][0]
        stack = []
    
    if not stack or stack[-1][1] < lst[n][1]:
        stack.append(lst[n])

if stack:
    result += stack[-1][1] - stack[0][0]

print(result)