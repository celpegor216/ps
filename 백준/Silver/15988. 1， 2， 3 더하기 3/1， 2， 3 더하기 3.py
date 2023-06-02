T = int(input())
    
memo = [0, 1, 2, 4]
    
for n in range(4, 1000001):
    memo.append((memo[n - 3] + memo[n - 2] + memo[n - 1]) % 1000000009)
    
for t in range(T):
    N = int(input())
        
    print(memo[N])