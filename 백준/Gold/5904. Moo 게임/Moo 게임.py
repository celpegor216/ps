N = int(input())

before = 0
now = 3
k = 0

while now < N:
    k += 1
    before = now
    now = before + k + 3 + before

result = ''

def fun(before, k):
    global result, N

    if result:
        return
    
    if N == before + 1:
        result = 'm'
    elif before + 1 < N <= before + k + 3:
        result = 'o'
    else:
        if N > before + k + 3:
            N -= (before + k + 3)
        fun((before - k - 2) // 2, k - 1)

fun(before, k)

print(result)