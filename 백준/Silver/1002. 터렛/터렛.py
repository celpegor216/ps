T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    # 두 번째 원이 반지름이 더 큰 원이 되도록
    if r1 > r2:
        x1, y1, r1, x2, y2, r2 = x2, y2, r2, x1, y1, r1

    # 원의 중심 간 거리
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    # 동심원
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)

    # 서로 떨어져 있는 경우
    elif dist > r1 + r2 or r2 > dist + r1:
        print(0)

    # 한 점에서 붙어있는 경우
    elif dist == r1 + r2 or r2 == dist + r1:
        print(1)

    # 그 외의 경우
    else:
        print(2)