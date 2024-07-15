# 유클리드 호제법을 쓰는 건 알겠는데 구현 방법을 모름
# 해답: https://donggyu.tistory.com/128

N = int(input())
lst_N = list(map(int, input().split()))
M = int(input())
lst_M = list(map(int, input().split()))

A = 1
for item in lst_N:
    A *= item
B = 1
for item in lst_M:
    B *= item

while B > 0:
    A, B = B, A % B

print(A if A < 10 ** 9 else str(A)[-9:])