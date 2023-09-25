# dp인 것 같은데 해결 방법을 모르겠음
# 해답: https://dleunji.tistory.com/68
# dp가 아닌 수학 문제였음,,,

# 값 1 => 최소 1, 최대 1
# 값 2 => 최소 2, 최대 2
# 값 3 => 최소 3, 최대 4
# 값 4 => 최소 5, 최대 6
# 값 5 => 최소 7, 최대 9
# 값 6 => 최소 10, 최대 12
# 값 7 => 최소 13, 최대 16
# 값 8 => 최소 17, 최대 20

# 값 2n => 최소 n ** 2 + 1, 최대 n(n+1)
# 값 2n + 1 => 최소 n(n+1) + 1, 최대 (n+1) ** 2


X, Y = map(int, input().split())

diff = Y - X

result = 0

if diff != result:
    while 1:
        if result ** 2 < diff <= result * (result + 1):
            result = 2 * result
            break
        
        if result * (result + 1) < diff <= (result + 1) ** 2:
            result = 2 * result + 1
            break

        result += 1

print(result)