N, M = map(int, input().split())
lst = [input() for _ in range(N)]

# 튜플 (A, B) < (C, D)이면 x > y, 즉 x의 우선순위가 더 높다
# 여기서 ai ≠ bi인 가장 작은 양의 정수 i에 대해
# ai < bi이면 (a1, ..., ak) < (b1, ..., bk)로 정의한다.

# 도로의 집합은 하나 이상의 도로가 우선순위에 대한 내림차순으로 정렬되어 있는 것
# 한 집합에 있는 도로만으로 임의의 도시에서 임의의 도시로 이동할 수 있을 때, 그 집합은 연결
# M개의 도로를 가진 도로의 집합 중 연결되어 있으면서 우선 순위가 가장 높은 것

# 번호가 작은 노드들부터 연결

group = [n for n in range(N)]

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

result = [0] * N
keep = []
cnt = 0

def union():
    global cnt

    for i in range(N - 1):
        for j in range(i + 1, N):
            if lst[i][j] == 'N':
                continue

            group_i, group_j = find(i), find(j)

            if group_i != group_j:
                cnt += 1
                result[i] += 1
                result[j] += 1

                if group_i > group_j:
                    group_i, group_j = group_j, group_i
                group[group_j] = group_i
            else:
                keep.append((i, j))

            if cnt == M:
                return

union()

if cnt < N - 1 or cnt + len(keep) < M:
    print(-1)
else:
    for i in range(M - cnt):
        a, b = keep[i]
        result[a] += 1
        result[b] += 1
    print(*result)
