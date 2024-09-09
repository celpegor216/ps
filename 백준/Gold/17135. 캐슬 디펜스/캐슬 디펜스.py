# 광진구 스터디 코드 리뷰 내용 참조


N, M, D = map(int, input().split())

# (i번 위치에서 적까지의 거리, 적의 x좌표, y좌표, 적의 번호) * 적의 수 만큼
distances_from_position_to_enemy = [[] for _ in range(M)]
# 적의 수
length = 0
for n in range(N):
    tmp = list(map(int, input().split()))

    for m in range(M):
        if not tmp[m]:
            continue

        for p in range(M):
            distances_from_position_to_enemy[p].append((N - n + abs(m - p), m, n, length))

        length += 1

for p in range(M):
    distances_from_position_to_enemy[p].sort()


def find_target(a, d):
    t = -1
    while a < length:
        if d[a][0] - n > D:
            break

        if d[a][2] >= N - n:
            a += 1
            continue

        if used[d[a][3]]:
            a += 1
            continue

        t = d[a][3]
        a += 1
        break

    return a, t

result = 0
for i in range(M - 2):
    d1 = distances_from_position_to_enemy[i]
    for j in range(i + 1, M - 1):
        d2 = distances_from_position_to_enemy[j]
        for k in range(j + 1, M):
            d3 = distances_from_position_to_enemy[k]

            # 죽은 적 체크
            used = [0] * length

            # 각 궁수 별 포인터
            a1 = a2 = a3 = 0

            for n in range(N):
                # 각 궁수 별 이번 턴의 타겟
                a1, t1 = find_target(a1, d1)
                a2, t2 = find_target(a2, d2)
                a3, t3 = find_target(a3, d3)

                for t in (t1, t2, t3):
                    if t != -1:
                        used[t] = 1

            result = max(result, used.count(1))

print(result)