T = int(input())

for _ in range(T):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    lst.sort()

    stack = []

    result = 0
    for _, num in lst:
        if stack and stack[-1] < num:
            result += 1
        else:
            stack.append(num)

    print(N - result)