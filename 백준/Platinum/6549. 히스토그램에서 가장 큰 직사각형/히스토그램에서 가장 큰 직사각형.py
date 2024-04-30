# 스택 같은데 풀이가 생각나지 않음
# 해답: https://velog.io/@e_juhee/python-%EB%B0%B1%EC%A4%80-6549-%ED%9E%88%EC%8A%A4%ED%86%A0%EA%B7%B8%EB%9E%A8%EC%97%90%EC%84%9C-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95

while 1:
    lst = list(map(int, input().split()))
    N = lst[0]

    if N == 0:
        break

    stack = []
    result = 0

    for n in range(1, N + 1):
        while stack and stack[-1][1] > lst[n]:
            idx, height = stack.pop()
            start = 1
            if stack:
                start = stack[-1][0] + 1
            result = max(result, (n - start) * height)

        if not stack or stack[-1][1] <= lst[n]:
            stack.append([n, lst[n]])
    
    while stack:
        idx, height = stack.pop()
        start = 1
        if stack:
            start = stack[-1][0] + 1
        result = max(result, (N + 1 - start) * height)

    print(result)