# 딕셔너리가 아닌 투포인터
# 해답: https://velog.io/@ckstn0778/%EB%B0%B1%EC%A4%80-7453%EB%B2%88-%ED%95%A9%EC%9D%B4-0%EC%9D%B8-%EB%84%A4-%EC%A0%95%EC%88%98-X-1

import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

ab = []
cd = []

for i in range(N):
    for j in range(N):
        ab.append(lst[i][0] + lst[j][1])
        cd.append(lst[i][2] + lst[j][3])

ab.sort()
cd.sort()

result = 0
i, j = 0, len(cd) - 1

while i < len(ab) and j >= 0:
    if ab[i] == -cd[j]:
        ni, nj = i + 1, j - 1
        while ni < len(ab) and ab[i] == ab[ni]:
            ni += 1
        while nj >= 0 and cd[j] == cd[nj]:
            nj -= 1
        
        result += (ni - i) * (j - nj)
        i, j = ni, nj
    elif ab[i] + cd[j] > 0:
        j -= 1
    else:
        i += 1

print(result)