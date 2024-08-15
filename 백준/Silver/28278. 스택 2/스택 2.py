import sys
input = sys.stdin.readline

N = int(input())

stack = []
result = []

for _ in range(N):
    command = input().split()

    if command[0] == '1':
        stack.append(int(command[1]))
    elif command[0] == '2':
        result.append(stack.pop() if stack else -1)
    elif command[0] == '3':
        result.append(len(stack))
    elif command[0] == '4':
        result.append(0 if stack else 1)
    elif command[0] == '5':
        result.append(stack[-1] if stack else -1)

for item in result:
    print(item)