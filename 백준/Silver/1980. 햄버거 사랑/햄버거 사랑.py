N, M, T = map(int, input().split())

maxb = 0
minc = T

# 타워 버거를 a개 먹었을 때
a = 0
while a * N <= T:
    burger = a
    time = T - a * N

    burger += time // M
    coke = time % M

    if coke < minc or (coke == minc and maxb < burger):
        minc = coke
        maxb = burger

    a += 1

print(maxb, minc)