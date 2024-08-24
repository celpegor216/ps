N = int(input())

for _ in range(N):
    R, E, C = map(int, input().split())

    if R > E - C:
        print('do not advertise')
    elif R < E - C:
        print('advertise')
    else:
        print('does not matter')