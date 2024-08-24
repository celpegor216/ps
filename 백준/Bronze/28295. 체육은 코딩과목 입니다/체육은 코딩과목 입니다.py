N = 10

directions = 'NESW'    # 시계 방향
d = 0

for _ in range(N):
    T = int(input())

    if T == 1:
        d = (d + 1) % 4
    elif T == 2:
        d = (d + 2) % 4
    else:
        d = (d - 1) % 4

print(directions[d])