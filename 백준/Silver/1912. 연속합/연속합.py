# 해답: https://bio-info.tistory.com/160

N = int(input())
lst = list(map(int, input().split()))

dp = [lst[0]]

for n in range(1, N):
    # dp[-1] + lst[n]: 이전 원소를 포함한 경우 최댓값
    # lst[n]: 이전 원소를 포함하지 않은 경우 최댓값
    dp.append(max(dp[-1] + lst[n], lst[n]))

print(max(dp))