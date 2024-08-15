A, B = map(int, input().split())

# 유클리드 호제법 구현 참고
# a와 b의 최대공약수 == b와 a % b의 최대공약수
# a % b가 0이 될 때의 a가 최대공약수
a, b = A, B
while b:
    a, b = b, a % b

print((A // a) * (B // a) * a)