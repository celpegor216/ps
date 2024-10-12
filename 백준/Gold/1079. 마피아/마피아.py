N = int(input())
lst = list(map(int, input().split()))
changes = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

# 만약 게임에 마피아가 한 명도 안 남았다면, 그 게임은 시민 팀이 이긴 것이고,
# 시민이 한 명도 안 남았다면, 그 게임은 마피아 팀이 이긴 것이다.
# 게임은 즉시 종료된다.

result = 0
def dfs(left, now, cnt):
    global result

    # 참가자가 홀수 명 남았을 때는 낮이다.
    # 낮에는 유죄 지수가 가장 높은 사람, 그 중에서 번호가 가장 작은 사람을 죽인다.
    if left % 2:
        max_v = -21e8
        max_idx = -1

        for key, value in now.items():
            if max_v < value:
                max_v = value
                max_idx = key
            elif max_v == value and max_idx > key:
                max_idx = key
        
        if max_idx == K:
            result = max(result, cnt)
            return

        nxt = {key:value for key, value in now.items() if key != max_idx}
        dfs(left - 1, nxt, cnt)

    # 참가자가 짝수 명 남았을 때는 밤이다.
    # 밤에는 마피아가 죽일 사람 한 명을 고른다. 죽은 사람은 게임에 더 이상 참여할 수 없다.
    # 참가자 i가 죽었다면 참가자 j의 유죄 지수는 changes[i][j]만큼 바뀐다.
    else:
        for target in now.keys():
            if target == K:
                continue

            nxt = {key: value + changes[target][key] for key, value in now.items() if key != target}
            dfs(left - 1, nxt, cnt + 1)


dfs(N, {idx: value for idx, value in enumerate(lst)}, 0)


print(result)