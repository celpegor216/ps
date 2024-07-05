N, M = map(int, input().split())

guitars = []

for _ in range(N):
    name, songs = input().split()
    guitars.append(songs)

result_songs = 0
result_cnt = -1

def dfs(level, start, songs, cnt):
    global result_songs, result_cnt
    
    if sum(songs) > result_songs or (sum(songs) == result_songs and cnt < result_cnt):
        result_songs = sum(songs)
        result_cnt = cnt

    for n in range(start, N):
        tmp = songs[:]
        for m in range(M):
            if guitars[n][m] == 'Y':
                tmp[m] = 1
        dfs(level + 1, n + 1, tmp, cnt + 1)
    
dfs(0, 0, [0] * M, 0)

print(result_cnt)