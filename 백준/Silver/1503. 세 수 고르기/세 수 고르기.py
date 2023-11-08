# 브루트포스 같은데 뭔가 놓치는 게 있는 것 같음
# 해답: https://ongveloper.tistory.com/474

N, M = map(int, input().split())
lst = list(map(int, input().split()))

result = 21e8

if M == 0:
    result = 0
else:
    for i in range(1, 1002):
        if i in lst:
            continue
        for j in range(1, 1002):
            if j in lst:
                continue
            for k in range(1, 1002):
                if k in lst:
                    continue

                result = min(result, abs(N - i * j * k))
                
                if N <= i * j * k:
                    break

print(result)