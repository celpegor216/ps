# 힌트: x이 알맞은 값이 나오려면 몇 번째 해가 되어야 하는지 먼저 구하기
# 답: https://ji-gwang.tistory.com/m/249

T = int(input())

for t in range(T):
    M, N, x, y = map(int, input().split())

    res = -1
    k = x

    while k <= M * N:
        if (k - x) % M == 0 and (k - y) % N == 0:
            res = k
            break
        k += M

    print(res)