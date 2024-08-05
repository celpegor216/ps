import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if lst[i][0] == lst[j][0] == lst[k][0] or lst[i][1] == lst[j][1] == lst[k][1]:
                continue

            i_to_j = (lst[i][0] - lst[j][0]) ** 2 + (lst[i][1] - lst[j][1]) ** 2
            i_to_k = (lst[i][0] - lst[k][0]) ** 2 + (lst[i][1] - lst[k][1]) ** 2
            j_to_k = (lst[j][0] - lst[k][0]) ** 2 + (lst[j][1] - lst[k][1]) ** 2

            if i_to_j + i_to_k == j_to_k or i_to_j + j_to_k == i_to_k or i_to_k + j_to_k == i_to_j:
                result += 1

print(result)