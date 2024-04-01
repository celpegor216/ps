N = int(input())
S = input()

result = -21e8

def calc(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    else:
        return a * b

def dfs(idx, now):
    global result

    if idx >= N - 1:
        tmp = []
        n = 0
        while n < N:
            if n in now:
                tmp.append(calc(int(S[n]), int(S[n + 2]), S[n + 1]))
                n += 3
            else:
                tmp.append(int(S[n]) if '0' <= S[n] <= '9' else S[n])
                n += 1

        res = tmp[0]
        i = 1
        while i < len(tmp):
            res = calc(res, tmp[i + 1], tmp[i])
            i += 2

        result = max(result, res)
        return
    
    dfs(idx + 2, now)
    dfs(idx + 4, now + [idx])

dfs(0, [])

print(result)