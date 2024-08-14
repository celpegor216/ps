T = int(input())

def dfs(now, path):
    global result

    if not now:
        return

    for key in now.keys():
        if not now[key][0]:
            result += 1
        else:
            if path + key in lst:
                result += 1
            dfs(now[key][1], path + key)

for _ in range(T):
    trie = dict()

    N = int(input())
    lst = []
    for n in range(N):
        S = input()
        lst.append(S)
        now = trie

        for s in S:
            if not now.get(s):
                now[s] = [0, dict()]
            now = now[s][1]

    M = int(input())
    for m in range(M):
        S = input()
        now = trie

        for s in S:
            if not now.get(s):
                now[s] = [1, dict()]
            now[s][0] = 1
            now = now[s][1]

    result = 0
    if M:
        dfs(trie, '')
    else:
        result = 1

    print(result)