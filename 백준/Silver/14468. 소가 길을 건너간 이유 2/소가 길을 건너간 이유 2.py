S = input()
N = 26

lst = [[-1] * 2 for _ in range(N)]
used = [0] * N * 2
for n in range(N * 2):
    if used[n]:
        continue

    used[n] = 1
    idx = ord(S[n]) - ord('A')
    if lst[idx][0] == -1:
        lst[idx][0] = n
    else:
        lst[idx][1] = n

result = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        si, ei = lst[i]
        sj, ej = lst[j]

        # 시작점이 i번째 소의 시작점과 종료점 사이에 있으면서
        # 종료점이 i번째 소의 시작점과 종료점 사이에 있지 않은 경우
        if (si < sj < ei and not (si < ej < ei)) or (not (si < sj < ei) and si < ej < ei):
            result += 1

print(result)