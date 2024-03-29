# 메모리 초과
# 해답: https://yhkim4504.tistory.com/11

N, M = map(int, input().split())
lst = [input() for _ in range(N)]
K = int(input())

result = 0
used = [0] * N

for n in range(N):
    if not used[n]:
        cnt_zero = lst[n].count('0')

        # K번 껐다 켜서 이 행을 모두 1로 만들 수 있다면
        # 이 행과 같은 모양의 행의 개수 구하기
        if cnt_zero <= K and cnt_zero % 2 == K % 2:
            cnt = 0
            for i in range(N):
                if lst[n] == lst[i]:
                    cnt += 1
                    used[i] = 1
            result = max(result, cnt)

print(result)