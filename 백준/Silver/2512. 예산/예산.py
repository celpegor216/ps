N = int(input())
lst = list(map(int, input().split()))
M = int(input())

if sum(lst) <= M:    # 모든 요청을 들어줄 수 있는 경우
    print(max(lst))
else:
    start = 1    # 상한액 최소 금액
    end = max(lst) - 1    # 상한액 최대 금액
    result = 0    # 상한액, 배정된 예산 중 최댓값

    while start <= end:
        middle = (start + end) // 2

        total = 0    # 상한액이 middle일 때 요청을 들어주기 위해 필요한 예산
        for item in lst:
            total += item if item <= middle else middle

        if total <= M:    # total이 실제 총 예산을 넘기지 않는 경우
            result = max(result, middle)
            start = middle + 1
        else:
            end = middle - 1

    print(result)