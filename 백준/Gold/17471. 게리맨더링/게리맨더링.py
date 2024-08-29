from collections import deque

# 구역을 두 개의 선거구로 나눠야 하고, 각 구역은 두 선거구 중 하나에 포함

N = int(input())
cnts = list(map(int, input().split()))    # 구역 별 인구 수
lst = [sorted([x - 1 for x in list(map(int, input().split()))[1:]]) for _ in range(N)]

total_cnt = result = sum(cnts)

# 선거구는 구역을 적어도 하나 포함해야 하고, 한 선거구에 포함되어 있는 구역은 모두 연결
# 임의의 구역(1)을 기준으로 연결할 수 있는 모든 조합 찾기
q = deque()
q.append(([0], cnts[0]))

used_combinations = set()
used_combinations.add((0, ))

while q:
    selected, total = q.popleft()

    if len(selected) == N:
        continue

    # 남은 선거구들이 하나로 연결되는지 확인
    not_selected = [n for n in range(N) if n not in selected]
    used_not_selected_cnt = 1
    nq = deque()
    nq.append(not_selected.pop(0))

    while nq:
        now = nq.popleft()

        for nxt in lst[now]:
            if nxt in not_selected and nxt not in selected:
                used_not_selected_cnt += 1
                nq.append(nxt)
                not_selected.remove(nxt)

    if used_not_selected_cnt == N - len(selected):
        result = min(result, abs((total_cnt - total) - total))

    for now in selected:
        for nxt in lst[now]:
            if nxt in selected:
                continue

            nxt_selected = selected + [nxt]
            nxt_tup = tuple(sorted(nxt_selected))

            if nxt_tup not in used_combinations:
                used_combinations.add(nxt_tup)
                q.append((nxt_selected, total + cnts[nxt]))

print(result if result != total_cnt else -1)