N = int(input())

for _ in range(N):
    M = int(input())
    # 킬 당 추가금 k, 데스 당 차감금 d, 어시스트 당 추가금 a
    lst = [list(map(int, input().split())) for _ in range(M)]
    K, D, A = map(int, input().split())

    result = 0
    for k, d, a in lst:
        tmp = K * k - D * d + A * a
        # 만약 어떤 미션의 계산 금액이 0보다 작은 경우에는 총 금액에 이를 합산하지 않는다
        if tmp > 0:
            result += tmp
    print(result)