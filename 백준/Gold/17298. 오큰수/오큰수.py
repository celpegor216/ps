# 힌트: 스택 사용

N = int(input())
lst = list(map(int, input().split()))

stack = [lst[-1]]
result = [-1] * N

for n in range(N - 2, -1, -1):
    while stack:
        if stack[-1] > lst[n]:
            result[n] = stack[-1]
            break
        else:
            stack.pop()
    
    stack.append(lst[n])

print(*result)