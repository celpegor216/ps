T = int(input())

def find(num):
    result = []

    for i in range(2, num + 1):
        while 1:
            if not num % i:
                result.append(i)
                num //= i
            else:
                break
    
    return result

for t in range(T):
    A, B = map(int, input().split())

    a = find(A)
    b = find(B)
    
    answer = 1

    for item in a:
        answer *= item
        if item in b:
            b.pop(b.index(item))

    for item in b:
        answer *= item
    
    print(answer)