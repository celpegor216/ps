N = int(input())

def is_prime(n):
    if n == 1:
        return 0

    half = int(n ** 0.5)

    for i in range(2, half + 1):
        if not n % i:
            return 0

    return 1

result = 0

while not result:
    if is_prime(N):
        tmp = str(N)
        flag = 0
        while tmp:
            if tmp[0] != tmp[-1]:
                flag = 1
                break
            tmp = tmp[1:len(tmp) - 1]
        
        if not flag:
            result = N
            break

    N += 1

print(result)