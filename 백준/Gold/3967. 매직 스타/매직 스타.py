N = 5
M = 9
T = 12    # 예제의 출력처럼 가장 작은 수부터 써도 가장 큰 수가 12이므로 1부터 12까지의 알파벳만 확인하면 됨

lst = [input() for _ in range(N)]
places = [0] * T  # 매직 스타의 위쪽부터, 왼쪽부터 순회하면서 채울 수 있는 공간
places_pos = []  # 이후에 다시 답을 채우기 위해 좌표 저장
lines = [
    [1, 2, 3, 4],    # 2번째 줄 가로
    [0, 2, 5, 7],    # 1번째 줄 > 4번째 줄 왼쪽 대각선
    [0, 3, 6, 10],    # 1번째 줄 > 4번째 줄 오른쪽 대각선
    [1, 5, 8, 11],   # 2번째 줄 > 5번째 줄 왼쪽 대각선
    [4, 6, 9, 11],   # 2번째 줄 > 5번째 줄 오른쪽 대각선
    [7, 8, 9, 10]    # 4번째 줄 가로
]
used_lines = [[] for _ in range(6)]    # 각 줄에 해당하는 수를 저장

idx = 0
used = [0] * (T + 1)
for n in range(N):
    for m in range(M):
        if lst[n][m] == 'x':  # 수가 채워져 있지 않은 곳
            idx += 1
            places_pos.append((n, m))
        elif lst[n][m] != '.':  # 수가 채워진 곳
            num = ord(lst[n][m]) - ord('A') + 1
            places[idx] = num
            used[num] = 1
            for i in range(6):
                if idx in lines[i]:
                    used_lines[i].append(num)
            idx += 1
            places_pos.append((n, m))

result = []

def dfs(level):
    global result

    if result:
        return

    if level == T:
        result = places[:]
        return

    if places[level]:    # 이미 채워져 있는 곳이면 스킵
        dfs(level + 1)
    else:                # 비어있다면 채우기
        for num in range(1, T + 1):
            if not used[num]:
                # 지금까지 채운 수들 중에서 확인할 수 있는 줄이 있으면 확인
                flag = 0
                for i in range(6):
                    if level in lines[i] and len(used_lines[i]) == 3:
                        if sum(used_lines[i]) + num != 26:
                            flag = 1
                            break

                if not flag:
                    used[num] = 1
                    places[level] = num
                    for i in range(6):
                        if level in lines[i]:
                            used_lines[i].append(num)
                    dfs(level + 1)
                    used[num] = 0
                    places[level] = 0
                    for i in range(6):
                        if level in lines[i]:
                            used_lines[i].remove(num)

dfs(0)

idx = 0
for i in range(N):
    for j in range(M):
        if idx == 12 or (i, j) != places_pos[idx]:
            print('.', end ='')
        else:
            print(chr(ord('A') + result[idx] - 1), end='')
            idx += 1
    print()