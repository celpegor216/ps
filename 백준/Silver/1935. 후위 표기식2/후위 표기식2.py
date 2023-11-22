N = int(input())
S = input()
dic = dict()

for n in range(N):
    dic[chr(ord('A') + n)] = int(input())

stack = []

for s in S:
    if dic.get(s):
        stack.append(dic[s])
    else:
        if s == '+':
            right = stack.pop()
            stack.append(stack.pop() + right)
        elif s == '-':
            right = stack.pop()
            stack.append(stack.pop() - right)
        elif s == '*':
            right = stack.pop()
            stack.append(stack.pop() * right)
        elif s == '/':
            right = stack.pop()
            stack.append(stack.pop() / right)  

print(f'{stack[0]:0.2f}')