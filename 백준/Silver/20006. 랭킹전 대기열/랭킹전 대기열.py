# 전체 플레이어 수, 방의 정원
N, M = map(int, input().split())

# rooms[i]: 기준 레벨, 입장한 플레이어의 인덱스 목록
rooms = []

for n in range(N):
    level, name = input().split()
    level = int(level)

    for i in range(len(rooms)):
        if rooms[i][0] - 10 <= level <= rooms[i][0] + 10 and len(rooms[i][1]) < M:
            rooms[i][1].append([level, name])
            break
    else:
        rooms.append([level, [[level, name]]])
    

for _, players in rooms:
    if len(players) == M:
        print('Started!')
    else:
        print('Waiting!')
    
    for player in sorted(players, key=lambda x: x[1]):
        print(*player)