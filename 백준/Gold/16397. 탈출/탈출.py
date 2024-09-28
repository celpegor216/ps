N, T, G = map(int, input().split())


def find():
    q = [N]

    MAX = 10 ** 5
    used = [0] * MAX
    used[N] = 1

    result = 0
    while q and result <= T:
        nq = []

        for now in q:
            if now == G:
                return result

            nxt = now + 1
            if nxt < MAX and not used[nxt]:
                used[nxt] = 1
                nq.append(nxt)
            
            nxt = now * 2
            if nxt >= MAX:
                continue

            tmp = list(str(nxt))
            for i in range(len(tmp)):
                if tmp[i] != '0':
                    tmp[i] = str(int(tmp[i]) - 1)
                    break
            
            nxt = int(''.join(tmp))
            if nxt < MAX and not used[nxt]:
                used[nxt] = 1
                nq.append(nxt)

        q = nq
        result += 1
    
    return 'ANG'


print(find())