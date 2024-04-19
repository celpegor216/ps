import sys
sys.setrecursionlimit(10 ** 5)

N = int(input())

def find(n):
    cnt = 0
    length = 0
    
    tmp = n
    while tmp:
        cnt += (tmp % 10) % 2
        tmp //= 10
        length += 1
    
    if n < 10:
        return cnt, cnt
    elif n < 100:
        res = find(n % 10 + n // 10)
        return cnt + res[0], cnt + res[1]
    else:
        maxv = 0
        minv = 21e8
        s = str(n)

        for i in range(1, length - 1):
            for j in range(i + 1, length):
                res = find(int(s[:i]) + int(s[i:j]) + int(s[j:]))
                minv = min(minv, res[0])
                maxv = max(maxv, res[1])
        
        return cnt + minv, cnt + maxv

print(*find(N))