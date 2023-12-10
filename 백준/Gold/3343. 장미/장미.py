# 이분탐색이 아니었음,,,
# 해답: https://welog.tistory.com/436

N, A, B, C, D = map(int, input().split())

if B / A > D / C:
    A, B, C, D = C, D, A, B

result = 10 ** 18

# 가성비가 안 좋은 C를 A개 미만으로 사는 것이 최저가로 구매하는 것
for a in range(A):
    left = N - a * C

    if left < 0:
        cnt = 0
    else:
        cnt = left // A if not left % A else left // A + 1

    result = min(result, cnt * B + a * D)

    if left < 0:
        break

print(result)