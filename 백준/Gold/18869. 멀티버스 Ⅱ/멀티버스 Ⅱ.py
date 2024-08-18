# 시간 초과
# 해답: https://velog.io/@723poil/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-18869-%EB%A9%80%ED%8B%B0%EB%B2%84%EC%8A%A4-2


import sys
input = sys.stdin.readline

M, N = map(int, input().split())

bucket = dict()

for _ in range(M):
    lst = list((map(int, input().split())))    # 중복 제거
    sorted_set = sorted(set(lst))
    rank = {sorted_set[i]: i for i in range(len(sorted_set))}    # 좌표 압축
    rank_tup = tuple([rank[item] for item in lst])
    bucket[rank_tup] = bucket.get(rank_tup, 0) + 1

result = 0
for value in bucket.values():
    result += value * (value - 1) // 2

print(result)