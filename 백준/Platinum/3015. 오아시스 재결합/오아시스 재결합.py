# 반례 참고

N = int(input())
lst = [int(input()) for _ in range(N)]

result = 0

stack = []

for n in range(N - 1, -1, -1):
    while stack and stack[-1][0] < lst[n]:
        result += stack.pop()[1]
    
    if stack and stack[-1][0] == lst[n]:
        stack[-1][1] += 1
        if len(stack) == 1:
            result += stack[-1][1] - 1
        else:
            result += stack[-1][1]
    else:
        if stack:
            result += 1
        stack.append([lst[n], 1])

print(result)