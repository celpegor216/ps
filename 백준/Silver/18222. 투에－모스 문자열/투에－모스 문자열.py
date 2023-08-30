K = int(input())

def func(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        s, e = 1, 100
        k = e

        while s <= e:
            m = (s + e) // 2

            if 2 ** m > n:
                k = min(k, m - 1)
                e = m - 1
            else:
                s = m + 1
        
        return 1 if func(n % (2 ** k)) == 0 else 0

print(func(K - 1))