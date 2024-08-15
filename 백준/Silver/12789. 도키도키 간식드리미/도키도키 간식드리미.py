N = int(input())
lst = list(map(int, input().split()))
lst.reverse()

stack = []

result = 'Nice'

idx = 1
while lst:
    if lst[-1] != idx:
        if not stack or stack[-1] != idx:
            stack.append(lst.pop())
        else:
            stack.pop()
            idx += 1
    else:
        lst.pop()
        idx += 1

while stack:
    if stack[-1] != idx:
        result = 'Sad'
        break
    stack.pop()
    idx += 1

print(result)