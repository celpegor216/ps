# 마포구 건물의 개수 N, 털린 금은방 S, 대도 X의 집 E, 앞으로 한 번에 달릴 수 있는 건물 수 F, 뒤로 한 번에 달릴 수 있는 건물 수 B, 마포구 경찰서의 개수 K
N, S, E, F, B, K = map(int, input().split())

used = [0] * (N + 1)
if K:
    for item in map(int, input().split()):
        used[item] = 1


def find():
    used[S] = 1
    q = [S]

    result = 0
    while q:
        nq = []

        for now in q:
            if now == E:
                return result
            
            for nxt in (now + F, now - B):
                if 1 <= nxt <= N and not used[nxt]:
                    used[nxt] = 1
                    nq.append(nxt)
        
        q = nq
        result += 1
    
    return 'BUG FOUND'


print(find())