N, M = map(int, input().split())
before = [list(map(int, input().split())) for _ in range(N)]
after = [list(map(int, input().split())) for _ in range(N)]

def grouping(lst):
    groups = []
    used = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if used[i][j]:
                continue

            q = [(i, j)]
            used[i][j] = 1
            idx = 0
            while idx < len(q):
                y, x = q[idx]

                for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] == lst[i][j]:
                        q.append((ny, nx))
                        used[ny][nx] = 1

                idx += 1

            groups.append(q)

    return groups

before_groups = grouping(before)

def check():
    changed_group = []

    for i in range(len(before_groups)):
        group = before_groups[i]
        is_changed = before[group[0][0]][group[0][1]] != after[group[0][0]][group[0][1]]
        after_changed = after[group[0][0]][group[0][1]]

        for j in range(1, len(group)):
            # 첫 번째 칸은 바뀌었는데 이 칸은 바뀌지 않았거나,
            # 첫 번째 칸은 그대로인데 이 칸은 바뀌었거나,
            # 백신을 놓은 후 같은 그룹인데 값이 달라졌다거나
            if is_changed != (before[group[j][0]][group[j][1]] != after[group[j][0]][group[j][1]]) or after[group[j][0]][group[j][1]] != after_changed:
                return 'NO'

        if is_changed:
            changed_group.append(i)

    # 바뀐 그룹이 여러 개인 경우
    if len(changed_group) > 1:
        return 'NO'

    return 'YES'

print(check())