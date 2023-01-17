# 주어진 중위 표기식을 연산자의 우선순위에 따라 괄호로 묶어준다. 그런 다음에 괄호 안의 연산자를 괄호의 오른쪽으로 옮겨주면 된다.
# 해답: https://velog.io/@enchantee/%EB%B0%B1%EC%A4%80-1918-Python

s = input()

stack = []
result = ''

for i in s:
    if 'A' <= i <= 'Z':
        result += i
    else:
        if i == '(':
            stack.append(i)
        elif i in ('*', '/'):
            while stack and stack[-1] in ('*', '/'):
                result += stack.pop()
            stack.append(i)
        elif i in ('+', '-'):
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

while stack:
    result += stack.pop()

print(result)
            