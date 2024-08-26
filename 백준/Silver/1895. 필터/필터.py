N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
T = int(input())

# 값이 T보다 크거나 같은 픽셀의 수
result = 0

# 필터의 가로 세로 크기
F = 3
# 필터에 있는 값들을 정렬했을 때 중앙값의 인덱스
middle = (F * F) // 2

for i in range(N - F + 1):
    for j in range(M - F + 1):
        tmp = []
        for f in range(F):
            tmp += lst[i + f][j:j + F]

        tmp.sort()

        if tmp[middle] >= T:
            result += 1

print(result)