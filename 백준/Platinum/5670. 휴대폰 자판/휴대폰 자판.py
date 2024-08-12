def dfs(now, cnt):
    global total

    flag = 1 if len(now.keys()) > 1 else 0

    for key in now.keys():
        if not key:
            total += cnt
        else:
            dfs(now[key], cnt + flag)

while 1:
    try:
        N = int(input())
        trie = dict()

        for _ in range(N):
            S = input()
            now = trie

            length = len(S)
            for i in range(length):
                if not now.get(S[i]):
                    now[S[i]] = dict()
                now = now[S[i]]
            now[''] = 1

        total = 0

        for key in trie.keys():
            dfs(trie[key], 1)

        print(f'{total / N:0.2f}')
    except:
        break