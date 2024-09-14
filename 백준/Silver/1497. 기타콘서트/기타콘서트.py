N, M = map(int, input().split())
lst = [set() for _ in range(N)]
for n in range(N):
    _, songs = input().split()

    for m in range(M):
        if songs[m] == 'Y':
            lst[n].add(m)

max_songs = 0
min_guitars = N

def dfs(level, guitars, songs):
    global max_songs, min_guitars

    length = len(songs)

    if length > max_songs or (length == max_songs and guitars < min_guitars):
        max_songs = length
        min_guitars = guitars

    if level == N:
        return
    
    # level번째 기타를 넣지 않음
    dfs(level + 1, guitars, songs)

    # level번째 기타를 넣음
    dfs(level + 1, guitars + 1, songs.union(lst[level]))

dfs(0, 0, set())

if max_songs > 0:
    print(min_guitars)
else:
    print(-1)