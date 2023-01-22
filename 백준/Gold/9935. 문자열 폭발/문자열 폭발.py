# 힌트: 스택 사용

s = input()
bomb = list(input())
length = len(bomb)

stack = []

for i in s:
    stack.append(i)
    if len(stack) >= length and stack[-length:] == bomb:
            for i in range(length):
                stack.pop()

if not stack:
    print('FRULA')
else:
    print(''.join(stack))