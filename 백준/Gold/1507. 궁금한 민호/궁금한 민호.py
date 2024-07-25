# 반례나 다른 해결 방법이 떠오르지 않음
# 해답: https://2hs-rti.tistory.com/entry/%EB%B0%B1%EC%A4%80-1507%EB%B2%88-%EA%B6%81%EA%B8%88%ED%95%9C-%EB%AF%BC%ED%98%B8-%ED%8C%8C%EC%9D%B4%EC%8D%AC

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

# i에서 j로 가는 도로가 최단인지 확인
used = [[1] * N for _ in range(N)]

result = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != k != j:
                # i에서 j까지 갈 때 k를 거쳐감 -> i에서 j까지 가는 도로는 사용하지 않음
                if lst[i][j] == lst[i][k] + lst[k][j]:
                    used[i][j] = 0
                # i에서 j까지 가는 것보다 k를 거쳐가는 게 더 빠름 -> i에서 j까지 가는 게 최소여야 하는데 잘못됨 == 답이 없는 경우
                elif lst[i][j] > lst[i][k] + lst[k][j]:
                    result = -1

if not result:
    for i in range(N):
        for j in range(i, N):
            if used[i][j]:
                result += lst[i][j]

print(result)