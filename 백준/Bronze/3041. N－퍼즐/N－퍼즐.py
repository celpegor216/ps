N = 4
lst = [input() for _ in range(4)]

result = 0

for i in range(N):
    for j in range(N):
        if lst[i][j] == '.':
            continue

        # expected_position: lst[i][j]가 원래 배열에서 있어야 하는 위치
        order = ord(lst[i][j]) - ord('A')
        expected_position = (order // N, order % N)

        result += abs(i - expected_position[0]) + abs(j - expected_position[1])

print(result)