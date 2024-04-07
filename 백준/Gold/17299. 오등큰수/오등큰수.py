N = int(input())
lst = list(map(int, input().split()))

bucket = [0] * 1000001
for item in lst:
    bucket[item] += 1

result = [-1] * N

stack = []

for n in range(N - 1, -1, -1):
    while stack:
        if bucket[stack[-1]] <= bucket[lst[n]]:
            stack.pop()
        else:
            break
    
    if stack:
        result[n] = stack[-1]
    
    stack.append(lst[n])

print(*result)