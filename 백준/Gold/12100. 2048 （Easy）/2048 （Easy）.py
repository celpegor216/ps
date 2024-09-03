N = int(input())
M = N

def move_arr(tlst):
    lst = [0 for _ in range(N)]
    idx = 0
    for i in range(N):
        if tlst[i] != 0:
            lst[idx] = tlst[i]
            idx += 1

    i = j = 0
    while 1:
        if j >= N: return lst
        
        #합쳐지는 경우
        if j+1<N and lst[j] == lst[j+1]:
            cnt = lst[j] + lst[j+1]
            lst[j] = lst[j+1] = 0
            lst[i] =cnt
            i += 1
            j += 2
        #안합쳐지는 경우
        else:
            if lst[i] == 0:
                lst[i] = lst[j]
                lst[j] = 0
            i += 1
            j += 1

def rotate(cnt, lst):
    for _ in range(cnt):
        lst = list(map(list, zip(*lst[::-1])))
    return lst


# dfs로 5번 이동
L = 5
result = 0
def dfs(level, lst):
    global result

    # 5번 움직인 이후에 격자판에서 가장 큰 값의 최댓값을 구하는 프로그램
    if level == L:
        for line in lst:
            result = max(result, max(line))
        return

    for i in range(4):
        # 90도 * i번 회전
        nxt = rotate(i, [line[:] for line in lst])

        for j in range(N):
            nxt[j] = move_arr(nxt[j])

        dfs(level + 1, nxt)


dfs(0, [list(map(int, input().split())) for _ in range(N)])
print(result)