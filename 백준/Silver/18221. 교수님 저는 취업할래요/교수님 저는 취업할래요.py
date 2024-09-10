N = int(input())
# 1은 성규가 아닌 학생, 2는 성규, 5는 교수님
lst = [list(map(int, input().split())) for _ in range(N)]

sy = sx = ey = ex = -1

for i in range(N):
    for j in range(N):
        if lst[i][j] == 2:
            sy, sx = i, j
        elif lst[i][j] == 5:
            ey, ex = i, j

def find():
    # 도망가는 데 성공하려면, 성규와 교수님의 거리가 5 이상이면서,
    # 이때, 책상 (a, b)와 책상 (c, d) 간의 거리는 sqrt{(a-c)^2 + (b-d)^2}로 정의
    if ((sy - ey) ** 2 + (sx - ex) ** 2) ** 0.5 < 5:
        return 0

    # 교수님과 성규를 꼭짓점으로 하는 축에 평행한 직사각형 안에, 교수님을 제지해줄 성규가 아닌 학생이 세 명 이상 있어야 한다.
    # 단, 교수님과 성규가 같은 행 혹은 같은 열의 책상에 앉아있다면 교수님과 성규를 잇는 선분 상에 성규가 아닌 학생이 세 명 이상 있어야 한다.
    cnt = 0
    miny = min(sy, ey)
    maxy = max(sy, ey)
    minx = min(sx, ex)
    maxx = max(sx, ex)

    for i in range(miny, maxy + 1):
        for j in range(minx, maxx + 1):
            if lst[i][j] == 1:
                cnt += 1

    if cnt < 3:
        return 0

    return 1


print(find())