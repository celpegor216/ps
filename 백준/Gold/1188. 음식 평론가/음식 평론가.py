# dp 같은데 규칙을 못 찾겠음
# M \ N | 1 2 3 4 5 6 7 8 9 10
#   1   | 0
#   2   | 1 0
#   3   | 2 2 0
#   4   | 3 2 3 0
#   5   | 4 4 4 4 0
#   6   | 5 4 3 4 5 0
#   7   | 6 6 6 6 6 6 0
#   8   | 7 6 7 4 7 6 7 0
#   9   | 8 8 6 8 8 6 8 8 0
#  10   | 9 8 9 8 5 8 9 8 9 0

# 해답: https://velog.io/@hyuntall/%EB%B0%B1%EC%A4%80-1188%EB%B2%88-%EC%9D%8C%EC%8B%9D-%ED%8F%89%EB%A1%A0%EA%B0%80-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# dp가 아닌 최대공약수 문제

N, M = map(int, input().split())

def gcd(a, b):
    if not a % b:
        return b
    return gcd(b, a % b)

print(M - gcd(N, M))