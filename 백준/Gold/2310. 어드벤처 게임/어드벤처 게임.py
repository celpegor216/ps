# 재방문 가능하게 처리했는데 왜 틀리는거지?
# 해답: https://magentino.tistory.com/227


# 초 기 값,,,,,,,, -1로 설정해야 하는구나,,,,,,,,,,,,,,,


import heapq


def find():
    if lst[1][0] < 0:
        return 'No'

    q = []
    heapq.heappush(q, (-lst[1][0], 1))
    used = [-1] * (N + 1)
    used[1] = lst[1][0]

    while q:
        cost, now = heapq.heappop(q)

        cost *= -1

        if used[now] > cost:
            continue

        if now == N:
            return 'Yes'
        
        for nxt in lst[now][1:]:
            nxt_cost = cost

            if lst[nxt][0] < 0:
                nxt_cost += lst[nxt][0]
            elif lst[nxt][0] > 0:
                nxt_cost = max(nxt_cost, lst[nxt][0])
            
            if nxt_cost < 0 or used[nxt] >= nxt_cost:
                continue
            
            used[nxt] = nxt_cost
            heapq.heappush(q, (-nxt_cost, nxt))
    

    return 'No'



while 1:
    N = int(input())

    if not N:
        break

    lst = [[]]
    for _ in range(N):
        room_type, *tmp = input().split()
        tmp = list(map(int, tmp))
        tmp.pop()
        if room_type == 'T':
            tmp[0] *= -1
        lst.append(tmp)

    print(find())