S = input()

stack = []
temp = []
idx = 0
length = len(S)

while idx < length:
    if S[idx] in ('(', '['):
        stack.append(S[idx])
        temp.append(0)
    else:
        if S[idx] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                num = temp.pop()
                now = num * 2 if num else 2
                if temp:
                    temp[-1] += now
                else:
                    temp.append(now)
            else:
                break
        else:
            if stack and stack[-1] == '[':
                stack.pop()
                num = temp.pop()
                now = num * 3 if num else 3
                if temp:
                    temp[-1] += now
                else:
                    temp.append(now)
            else:
                break
    idx += 1

if idx < length or stack:
    print(0)
else:
    print(sum(temp))