N, P = map(int, input().split())
now = N    # 현재 값

# 출력되는 순서대로 used 배열에 저장
# 처음에는 N을 출력함
used = [N]

while 1:
    now = (now * N) % P

    # 사이클을 발견한 것이므로 종료
    if now in used:
        break

    used.append(now)

# now에 있는 수가 사이클이 시작하는 지점이므로
# 전체 used의 길이에서 now의 위치를 빼주면
# 사이클의 길이가 구해짐
print(len(used) - used.index(now))