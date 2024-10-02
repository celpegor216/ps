N, R = map(int, input().split())
N = 2 ** N
lst = [list(map(int, input().split())) for _ in range(N)]


def reverse_inside(L):
    new_lst = []
    for i in range(0, N, L):
        for l in range(L - 1, -1, -1):
            new_lst.append(lst[i + l])
    return new_lst


def rotate_inside(L, direction):
    for i in range(0, N, L):
        for j in range(0, N, L):
            tmp = [lst[i + l][j:j + L] for l in range(L)]
            if direction == 1:    # 오른쪽 90도
                tmp = list(map(list, zip(*tmp[::-1])))
            else:    # 왼쪽 90도
                tmp = list(map(list, zip(*tmp)))[::-1]
            for l in range(L):
                lst[i + l][j:j + L] = tmp[l]


def reverse_parts(L):
    new_lst = []
    for i in range(N - L, -1, -L):
        for l in range(L):
            new_lst.append(lst[i + l])
    return new_lst


def rotate_parts_right(L):
    tmp_lst = []
    for j in range(0, N, L):
        tmp_lst.append([])
        for i in range(N - L, -1, -L):
            tmp_lst[-1].append([lst[i + l][j:j + L] for l in range(L)])
    new_lst = [[] for _ in range(N)]
    M = N // L
    for i in range(M):
        for j in range(M):
            for l in range(L):
                new_lst[i * L + l] += tmp_lst[i][j][l]
    return new_lst


def rotate_parts_left(L):
    tmp_lst = []
    for j in range(N - L, -1, -L):
        tmp_lst.append([])
        for i in range(0, N, L):
            tmp_lst[-1].append([lst[i + l][j:j + L] for l in range(L)])

    new_lst = [[] for _ in range(N)]
    M = N // L
    for i in range(M):
        for j in range(M):
            for l in range(L):
                new_lst[i * L + l] += tmp_lst[i][j][l]
    return new_lst


for _ in range(R):
    K, L = map(int, input().split())
    L = 2 ** L

    if K == 1:
        if L == 1:
            continue
        lst = reverse_inside(L)

    elif K == 2:
        if L == 1:
            continue
        lst = list(map(list, zip(*lst)))
        lst = reverse_inside(L)
        lst = list(map(list, zip(*lst)))

    elif K == 3:
        if L == 1:
            continue
        rotate_inside(L, 1)

    elif K == 4:
        if L == 1:
            continue

        rotate_inside(L, -1)

    elif K == 5:
        lst = reverse_parts(L)

    elif K == 6:
        lst = list(map(list, zip(*lst)))
        lst = reverse_parts(L)
        lst = list(map(list, zip(*lst)))

    elif K == 7:
        lst = rotate_parts_right(L)

    elif K == 8:
        lst = rotate_parts_left(L)

for line in lst:
    print(*line)