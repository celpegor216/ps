# 해답: https://dreamtreeits.tistory.com/32

N, M = map(int, input().split())
truth = set(list(map(int, input().split()))[1:])
party = [set(list(map(int, input().split()))[1:]) for _ in range(M)]
cnt = [1] * M

for m in range(M):
    for idx, people in enumerate(party):
        if truth & people:
            cnt[idx] = 0
            truth |= people

print(sum(cnt))