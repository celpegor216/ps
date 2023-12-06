# 왜 플로이드 워셜은 안 되는 거지?
# 해답: https://velog.io/@soobin519/Python-%EB%B0%B1%EC%A4%80-11657%ED%83%80%EC%9E%84%EB%A8%B8%EC%8B%A0%EB%B2%A8%EB%A7%8C%ED%8F%AC%EB%93%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%9D%B4%EB%A1%A0

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

result = [21e10] * (N + 1)

def bf(start):
    result[start] = 0

    for i in range(N):
        for a, b, c in edges:
            if result[a] != 21e10 and result[b] > result[a] + c:
                result[b] = result[a] + c
                if i == N - 1:
                    return True
    
    return False

has_negative_cycle = bf(1)

if has_negative_cycle:
    print(-1)
else:
    for n in range(2, N + 1):
        print(result[n] if result[n] != 21e10 else -1)