# 이항 계수: 주어진 집합(N)에서 원하는 개수(K)만큼 순서없이 뽑는 조합의 개수

N, K = map(int, input().split())

a = 1
b = 1

for n in range(N - K + 1, N + 1):
    a *= n

for n in range(1, K + 1):
    b *= n

print((a // b) % 10007)