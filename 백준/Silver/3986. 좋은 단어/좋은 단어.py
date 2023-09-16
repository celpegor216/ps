N = int(input())
lst = [input() for _ in range(N)]

result = 0

for n in range(N):
    length = len(lst[n])

    if length % 2:
        continue

    stack = []
    for m in range(length):
        if lst[n][m] == 'A':
            if stack and stack[-1] == 'A':
                stack.pop()
            else:
                stack.append('A')
        else:
            if stack and stack[-1] == 'B':
                stack.pop()
            else:
                stack.append('B')

    if not stack:
        result += 1

print(result)