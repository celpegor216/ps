N = int(input())
lst = [[0] * N for _ in range(N)]
students = dict()
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for n in range(N ** 2):
    tmp = list(map(int, input().split()))
    now = tmp[0]
    favs = tmp[1:]
    students[now] = favs

    if n == 0:
        lst[1][1] = tmp[0]
    else:
        cnt_fav = cnt_blank = 0
        idx = [21e8, 21e8]

        for i in range(N):
            for j in range(N):
                if not lst[i][j]:
                    tmp_cnt_fav = tmp_cnt_blank = 0

                    for d in range(4):
                        ni, nj = i + dy[d], j + dx[d]
                        if 0 <= ni < N and 0 <= nj < N:
                            if lst[ni][nj] in favs:
                                tmp_cnt_fav += 1
                            elif not lst[ni][nj]:
                                tmp_cnt_blank += 1
                    
                    if tmp_cnt_fav > cnt_fav:
                        cnt_fav = tmp_cnt_fav
                        cnt_blank = tmp_cnt_blank
                        idx = [i, j]
                    elif tmp_cnt_fav == cnt_fav:
                        if tmp_cnt_blank > cnt_blank:
                            cnt_blank = tmp_cnt_blank
                            idx = [i, j]
                        elif tmp_cnt_blank == cnt_blank:
                            if idx[0] > i:
                                idx = [i, j]
                            elif idx[0] == i:
                                if idx[1] > j:
                                    idx[1] = j
        
        lst[idx[0]][idx[1]] = now

result = 0

for i in range(N):
    for j in range(N):
        cnt = 0

        for d in range(4):
            ni, nj = i + dy[d], j + dx[d]
            if 0 <= ni < N and 0 <= nj < N and lst[ni][nj] in students[lst[i][j]]:
                cnt += 1
        
        if cnt:
            result += 10 ** (cnt - 1)

print(result)