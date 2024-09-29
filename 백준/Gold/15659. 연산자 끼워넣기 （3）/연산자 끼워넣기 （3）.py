N = int(input())
lst = list(map(int, input().split()))
calcs = list(map(int, input().split()))


# 연산자 우선 순위를 이용해 계산, 우선 순위가 같은 경우에는 앞에 있는 식을 먼저 계산
# 나눗셈은 정수 나눗셈으로 몫만 취한다
minv = 21e8
maxv = -21e8
def calculate(path):
    global minv, maxv

    # 곱셈/나눗셈 > 덧셈/뺄셈
    stack = [[-1, lst[0]]]
    for n in range(N - 1):
        if path[n] == 0:
            stack.append([0, lst[n + 1]])
        elif path[n] == 1:
            stack.append([1, lst[n + 1]])
        elif path[n] == 2:
            stack[-1][-1] *= lst[n + 1]
        elif path[n] == 3:
            stack[-1][-1] //= lst[n + 1]
    
    for i in range(1, len(stack)):
        if stack[i][0] == 0:
            stack[0][1] += stack[i][1]
        else:
            stack[0][1] -= stack[i][1]

    minv = min(minv, stack[0][1])
    maxv = max(maxv, stack[0][1])


def dfs(level, path):
    if level == N - 1:
        calculate(path)
        return

    for i in range(4):
        if calcs[i]:
            calcs[i] -= 1
            dfs(level + 1, path + [i])
            calcs[i] += 1


dfs(0, [])

print(maxv)
print(minv)