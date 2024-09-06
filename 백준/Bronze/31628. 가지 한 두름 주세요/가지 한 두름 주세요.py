N = 10
lst = [input().split() for _ in range(N)]

def check(tmp):
    for i in range(N):
        for j in range(1, N):
            if tmp[i][0] != tmp[i][j]:
                break
        else:
            return 1
    return 0

print(1 if check(lst) or check(list(zip(*lst))) else 0)