N = int(input())
lst = [input().split() for _ in range(N)]

time = 0    # 현재 시각
direction = 1    # 현재 시각이 흐르는 방향

for card_type, num in lst:
    time += direction

    if time == 13:
        time = 1
    elif time == 0:
        time = 12

    num = int(num)

    # 동기화의 법칙: 플레이어가 외친 시각과 펼쳐진 카드에 적힌 시각이 일치하면, 모든 플레이어들은 즉시 손바닥으로 게임판 중앙을 내리쳐야 합니다.
    if card_type != 'HOURGLASS' and time == num:
        print(time, 'YES')
    else:
        # 시간 역행의 법칙: 누군가 모래시계 카드를 펼치면 시간이 거꾸로 흐르기 시작합니다. "2시", "1시", "12시" 순으로 외쳐야 합니다. 모래시계 카드가 펼쳐질 때마다 시간의 흐름은 반전됩니다.
        if card_type == 'HOURGLASS' and time != num:
            direction *= -1
        print(time, 'NO')