L, N, T = map(int, input().split())
# i번째 공의 위치 S, 방향 C
lst = []
for _ in range(N):
    S, C = input().split()
    S = int(S)
    C = 1 if C == 'R' else -1
    lst.append((S, C))

# 위치 오름차순 정렬
lst.sort()

result = 0
for _ in range(T):
    used = [0] * (L + 1)
    for n in range(N):
        position, direction = lst[n]
        position += direction

        # 벽에 충돌한 경우
        if position in (0, L):
            direction *= -1
        # 벽이 아닌 다른 공에 충돌한 경우
        elif used[position]:
            result += 1
        
        used[position] = 1

        lst[n] = [position, direction]

print(result)