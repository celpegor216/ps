# 자른 나무를 팔았을 때 이익이 발생하지 않을 수도 있음
# 해답: https://fre2-dom.tistory.com/407

N, C, W = map(int, input().split())
lst = [int(input()) for _ in range(N)]

result = 0

for i in range(1, max(lst) + 1):
    total = 0

    for item in lst:
        tmp = 0
        tmp += (item // i) * i * W

        cnt = item // i
        if not item % i:
            cnt -= 1
        tmp -= cnt * C

        if tmp > 0:
            total += tmp
    
    result = max(result, total)

print(result)