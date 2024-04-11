# 누적합 같은데 방법을 모르겠음
# 해답: https://rapun7el.tistory.com/158

N, K = map(int, input().split())
lst = list(map(int, input().split()))

# 누적합
sum_lst = [0] * N
for n in range(N):
    sum_lst[n] = sum_lst[n - 1] + lst[n]

# 누적합 - 평균 * 구간길이
diff_lst = [0] * N
for n in range(N):
    diff_lst[n] = sum_lst[n] - K * (n + 1)

diff_bucket = dict()
for diff in diff_lst:
    diff_bucket[diff] = diff_bucket.get(diff, 0) + 1

# 차이값이 같은 두 구간 사이의 평균은 0
result = diff_bucket.get(0, 0)
for value in diff_bucket.values():
    result += value * (value - 1) // 2

print(result)