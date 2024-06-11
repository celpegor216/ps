S = input()
length = len(S)

stack = []
result = 0
idx = 0

while idx < length:
    if S[idx:idx + 2] == '()':
        for i in range(len(stack)):
            stack[i] += 1
        idx += 1
    elif S[idx] == '(':
        stack.append(1)
    else:
        result += stack.pop()
    idx += 1

print(result)