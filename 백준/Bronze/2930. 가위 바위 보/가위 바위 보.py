R = int(input())
S = input()
N = int(input())

key_wins_value = {'R': 'S', 'S': 'P', 'P': 'R'}
char_to_idx = {'R': 0, 'S': 1, 'P': 2}
cnts = [[0] * 3 for _ in range(R)]

original_result = 0
for _ in range(N):
    tmp = input()

    for r in range(R):
        if key_wins_value[S[r]] == tmp[r]:
            original_result += 2
        elif S[r] == tmp[r]:
            original_result += 1
        cnts[r][char_to_idx[tmp[r]]] += 1

print(original_result)

best_result = 0
for r in range(R):
    maxv = 0
    for i in range(3):
        total = 0
        for j in range(3):
            total += cnts[r][(i + j) % 3] * j
        maxv = max(maxv, total)
    best_result += maxv

print(best_result)