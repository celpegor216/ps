# 힌트: 그리디
# 해답: https://journeytosth.tistory.com/16

N = int(input())
K = int(input())
lst = sorted(map(int, input().split()))

dist = []

for n in range(N - 1):
    dist.append(lst[n + 1] - lst[n])

print(sum(sorted(dist)[:N - K]))