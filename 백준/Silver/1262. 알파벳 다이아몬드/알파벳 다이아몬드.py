N, u, l, d, r = map(int, input().split())
size = 2 * N - 1


def find(i, j):
    if i + j < N - 1:
        return '.'
    chr_idx = ((N - 1) * 2 - (i + j)) % 26
    return chr(ord('a') + chr_idx)


for i in range(u, d + 1):
    ni = i % size
    if ni >= N:
        ni = N - 2 - (ni % N)
    
    for j in range(l, r + 1):
        nj = j % size
        if nj >= N:
            nj = N - 2 - (nj % N)
        print(find(ni, nj), end='')
    print()