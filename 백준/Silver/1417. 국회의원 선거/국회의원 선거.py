import heapq

N = int(input())
cnt = 0

if N > 1:
    q = []

    heapq.heapify(q)

    dasom = int(input())

    for n in range(N - 1):
        heapq.heappush(q, -int(input()))


    while 1:
        rival = heapq.heappop(q)

        if -rival < dasom:
            break
        else:
            rival += 1
            dasom += 1
            cnt += 1
            heapq.heappush(q, rival)

print(cnt)