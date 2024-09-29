# 스택같은데 모르겠다,,,
# 해답: https://frog-in-well.tistory.com/33


# 좌표 압축,,,


N = int(input())
lst = []
pos = set()

for _ in range(N):
    s, e = map(int, input().split())
    lst.append((s, e))
    pos.add(s)
    pos.add(e)

pos = sorted(pos)
pos_dict = dict()
for idx, value in enumerate(pos):
    pos_dict[value] = idx

result = [-1] * len(pos)
for n in range(N):
    l, r = lst[n]
    dl, dr = pos_dict[l], pos_dict[r]
    for k in range(dl, dr + 1):
        result[k] = n

print(len(set(result)))