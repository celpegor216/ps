N = int(input())
lst = list(map(int, input().split()))

result = [0] * N
stack = []

for n in range(N - 1, -1, -1):
    while stack and lst[stack[-1]] < lst[n]:
        result[stack.pop()] = n + 1

    stack.append(n)

print(*result)