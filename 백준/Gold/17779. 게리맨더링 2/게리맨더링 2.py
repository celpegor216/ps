# 크기가 N×N
N = int(input())
# 구역 (r, c)의 인구는 A[r][c]
# 선거구의 인구는 선거구에 포함된 구역의 인구를 모두 합한 값
# 좌표 헷갈려서 패딩 추가함
lst = [[0] * (N + 1)]
for _ in range(N):
    lst.append([0] + list(map(int, input().split())))

# 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값
result = N * N * 100

def check(x, y, d1, d2):
    global result

    # 다섯 개의 선거구
    # 선거구는 구역을 적어도 하나 포함, 한 선거구에 포함되어 있는 구역은 모두 연결
    areas = [0] * 5

    # 기준점 (x, y)와 경계의 길이 d1, d2
    # 경계선과 경계선의 안에 포함되어있는 곳은 5번 선거구
    used = [[0] * (N + 1) for _ in range(N + 1)]

    # (x, y), (x+1, y-1), ..., (x+d1, y-d1)
    # (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)
    for i in range(d1 + 1):
        used[x + i][y - i] = 1
        used[x + d2 + i][y + d2 - i] = 1

    # (x, y), (x+1, y+1), ..., (x+d2, y+d2)
    # (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
    for i in range(d2 + 1):
        used[x + i][y + i] = 1
        used[x + d1 + i][y - d1 + i] = 1

    for i in range(1, N + 1):
        s = e = 0

        for j in range(1, N + 1):
            if used[i][j]:
                if not s:
                    s = j
                else:
                    e = j

        if not e:
            e = s

        for j in range(1, N + 1):
            if s <= j <= e:
                areas[4] += lst[i][j]
            else:
                # 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
                if 1 <= i < x + d1 and 1 <= j <= y:
                    areas[0] += lst[i][j]
                # 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
                elif 1 <= i <= x + d2 and y < j <= N:
                    areas[1] += lst[i][j]
                # 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
                elif x + d1 <= i <= N and 1 <= j < y - d1 + d2:
                    areas[2] += lst[i][j]
                # 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
                elif x + d2 < i <= N and y - d1 + d2 <= j <= N:
                    areas[3] += lst[i][j]

    result = min(result, max(areas) - min(areas))

# 기준점 정하기
for i in range(1, N - 1):
    for j in range(2, N):

        # 기준점 별 경계의 길이 정하기
        # d1, d2는 각각 최소 1이어야 하고 d1 + d2의 최대는 N - i - 1
        MAX = N - i
        for d1 in range(1, min(j, MAX)):
            for d2 in range(1, min(N - j, MAX - d1) + 1):
                # 계산
                check(i, j, d1, d2)

print(result)