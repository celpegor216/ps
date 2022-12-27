# 해답: https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-1629%EB%B2%88-%EA%B3%B1%EC%85%88-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython

A, B, C = map(int, input().split())

lst = [-1]

def multiply(a, b):
    if b == 1:
        return a % C

    temp = multiply(a, b // 2)

    # 지수가 짝수인 경우
    if not b % 2:
        return (temp * temp) % C
    # 지수가 홀수인 경우
    return (temp * temp * a) % C

print(multiply(A, B))