N = int(input())
lst = [0] + list(map(int, input().split()))

Q = int(input())
for _ in range(Q):
    t, n = map(int, input().split())

    if t == 1:    # n의 배수 스위치 상태를 바꿈
        i = n
        while i <= N:
            lst[i] ^= 1
            i += n
    else:    # n을 기준으로 대칭이 깨질 때까지 범위를 넓히면서 스위치 상태를 바꿈
        lst[n] ^= 1
        dist = 1
        while n - dist > 0 and n + dist <= N and lst[n - dist] == lst[n + dist]:
            lst[n - dist] ^= 1
            lst[n + dist] ^= 1
            dist += 1

# 1번 스위치부터 시작해서 한 줄에 20개씩 출력...
for i in range(1, N + 1, 20):
    if i + 20 <= N:
        print(*lst[i: i + 20])
    else:
        print(*lst[i:])