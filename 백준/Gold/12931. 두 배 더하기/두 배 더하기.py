# 힌트: 그리디
# 해답 참조

N = int(input())
A = [0] * N
B = list(map(int, input().split()))

result = 0

while B != A:
    for n in range(N):
        if B[n] % 2:
            B[n] -= 1
            result += 1
    
    flag = 0
    for n in range(N):
        if B[n]:
            B[n] //= 2
            flag = 1
    
    if flag:
        result += 1

print(result)