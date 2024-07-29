N = int(input())
target = [int(input()) for _ in range(N)]

num = 0
stack = []
result = []

for i in range(N):
    while 1:
        if len(stack) == 0 or (stack[-1] < target[i] and num < target[i]):
            num += 1
            stack.append(num)
            result.append('+')
        else:
            if stack[-1] == target[i]:
                stack.pop()
                result.append('-')
                break
            else:
                result = ['NO']
                break

    if result[0] == 'NO':
        break

for item in result:
    print(item)