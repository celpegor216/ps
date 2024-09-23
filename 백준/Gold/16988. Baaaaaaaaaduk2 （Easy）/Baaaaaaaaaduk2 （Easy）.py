N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

# 2의 그룹 중 빈 칸이 2개 이하인 그룹을 찾고
# [그룹에 속한 돌의 수, [채워야하는 칸 좌표]] 저장하기
possible_groups = []
possible_blanks = set()
used = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if lst[i][j] != 2 or used[i][j]:
            continue

        q = [(i, j)]
        used[i][j] = 1
        cnt = 1
        blanks = set()

        while q:
            nq = []

            for y, x in q:
                for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ny, nx = y + dy, x + dx
                    if not (0 <= ny < N and 0 <= nx < M) or lst[ny][nx] == 1 or used[ny][nx]:
                        continue

                    if lst[ny][nx] == 2:
                        used[ny][nx] = 1
                        nq.append((ny, nx))
                        cnt += 1
                    elif lst[ny][nx] == 0:
                        blanks.add((ny, nx))

            q = nq

        if len(blanks) <= 2:
            possible_groups.append((cnt, blanks))
            possible_blanks |= blanks


possible_blanks = list(possible_blanks)
length = len(possible_blanks)

result = 0
if length < 2:
    for cnt, _ in possible_groups:
        result += cnt
else:
    for i in range(length - 1):
        for j in range(i + 1, length):
            now = [possible_blanks[i], possible_blanks[j]]
            total = 0
            for cnt, blanks in possible_groups:
                for blank in blanks:
                    if blank not in now:
                        break
                else:
                    total += cnt

            result = max(result, total)
print(result)