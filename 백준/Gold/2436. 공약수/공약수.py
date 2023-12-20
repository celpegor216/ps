A, B = map(int, input().split())

left = B // A
half = int(left ** 0.5) + 1

result = 21e8
result_i = 0
result_j = 0

# 유클리드 호제법 필요
# 구현 참고: https://velog.io/@jwisgenius/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

for i in range(1, half):
    if not left % i:
        j = left // i

        # i와 j가 서로소여야 함
        flag = gcd(i, j)

        if result > j - i and flag == 1:
            result = j - i
            result_i = i
            result_j = j

print(result_i * A, result_j * A)