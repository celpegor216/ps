# 이분탐색으로 접근했으나 실패함
# 해답: https://sodehdt-ldkt.tistory.com/54

N, K = map(int, input().split())
lst = list(map(int, input().split()))
diff = []
for n in range(N - 1):
    diff.append(lst[n + 1] - lst[n])

diff.sort()

print(sum(diff[:N - K]))