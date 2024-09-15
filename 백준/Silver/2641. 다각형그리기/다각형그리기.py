# 오른쪽, 위쪽, 왼쪽, 아래쪽
directions_oppo = (0, 3, 4, 1, 2)
N = int(input())
original = list(map(int, input().split()))
reversed_original = [directions_oppo[item] for item in original[::-1]]

possibles = []

for n in range(1, N + 1):
    possibles.append(original[-n:] + original[:-n])
    possibles.append(reversed_original[-n:] + reversed_original[:-n])

Q = int(input())
result = []
for _ in range(Q):
    lst = list(map(int, input().split()))
    if lst in possibles:
        result.append(lst)

print(len(result))
for res in result:
    print(*res)