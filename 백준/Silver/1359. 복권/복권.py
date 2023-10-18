N, M, K = map(int, input().split())

# N개 중에 M개를 뽑는 경우의 수
total = 1

for m in range(1, M + 1):
    total *= (N - m + 1)
    total /= m

# K개 이상 겹치는 경우의 수
# 수식을 어떻게 세워야하는지 모르겠음
# 해답: https://ongveloper.tistory.com/468
# 뽑은 M개 중에서 K개 이상을 선택하는 경우의 수를 모두 구해서 더하면 하면 된다...!
# 겹치는 것 * 안 겹치는 것
# => M개 중에서 K개 선택 * (N - M)개 중에서 (M - K)개 선택

cross = 0

for k in range(K, M + 1):
    tmp = 1

    for m in range(1, k + 1):
        tmp *= (M - m + 1)
        tmp /= m

    for m in range(1, M - k + 1):
        tmp *= (N - M - m + 1)
        tmp /= m
    
    cross += tmp

print(cross / total)