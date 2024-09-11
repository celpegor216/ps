N, M = map(int, input().split())
lst = [input() + '#' for _ in range(N)] + ['#' * (M + 1)]


results = set()
for i in range(N + 1):
    # 만약 그 칸이 가로로 이어지는 단서의 시작점이면
    # 그 칸은 비어있으면서 왼쪽 칸이 막혀있거나 격자 밖이어야 하고,
    # 오른쪽에 있는 두 개 이상의 칸은 비어있어야한다
    # (가로로 이어지는 말은 3글자 이상이라는 것을 알 수 있다).
    cnt = 0
    for j in range(M + 1):
        if lst[i][j] == '#':
            if cnt > 2:
                results.add((i + 1, j - cnt + 1))
            cnt = 0
        else:
            cnt += 1


for j in range(M + 1):
    # 만약 그 칸이 세로로 이어지는 단서의 시작점일 경우
    # 그 칸은 비어있으면서 그 위의 칸은 막혀있거나 격자의 바깥이며,
    # 아래로 두 개 이상의 칸은 비어있어야 한다.
    cnt = 0
    for i in range(N + 1):
        if lst[i][j] == '#':
            if cnt > 2:
                results.add((i - cnt + 1, j + 1))
            cnt = 0
        else:
            cnt += 1


print(len(results))
# 번호는 책을 읽는 순서와 동일하게 왼쪽 위부터 오른쪽 아래까지 행 우선으로 순서대로 매긴다.
for result in sorted(results):
    print(*result)
