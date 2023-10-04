N = int(input())
lst = list(map(int, input().split()))

stack = []

result = [0] * N

for n in range(N - 1, -1, -1):
    while stack:
        if lst[stack[-1]] < lst[n]:
            result[stack.pop()] = n + 1
        else:
            break

    stack.append(n)

print(*result)