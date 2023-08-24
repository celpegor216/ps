S = input()

stack = []
result = ''

idx = 0
for i in range(len(S)):
    if S[i] == '>':
        start = stack.pop()
        result += S[start:i + 1]
        idx = i + 1
    elif S[i] == '<':
        result += S[idx:i][::-1]
        stack.append(i)
    elif not stack and S[i] == ' ':
        result += S[idx:i][::-1] + ' '
        idx = i + 1

if idx != len(S):
    result += S[idx:i+1][::-1]
print(result)