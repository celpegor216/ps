# 해답: https://ku-hug.tistory.com/122

# N이 홀수일 때
# Fn = (F(n//2+1) ** 2) + (F(n//2) ** 2)

# N이 짝수일 때
# Fn = (F(n//2+1) ** 2) - (F(n//2-1) ** 2)

N = int(input())

dp = dict()

mod = 1000000007

def fibo(n):
    if dp.get(n):
        return dp[n]
    
    if n == 0:
        return 0
    
    if n in (1, 2):
        return 1
    
    if not n % 2:
        dp[n // 2 + 1] = fibo(n // 2 + 1) % mod
        dp[n // 2 - 1] = fibo(n // 2 - 1) % mod
        return dp[n // 2 + 1] ** 2 - dp[n // 2 - 1] ** 2
    else:
        dp[n // 2 + 1] = fibo(n // 2 + 1) % mod
        dp[n // 2] = fibo(n // 2) % mod
        return dp[n // 2 + 1] ** 2 + dp[n // 2] ** 2

print(fibo(N) % mod)