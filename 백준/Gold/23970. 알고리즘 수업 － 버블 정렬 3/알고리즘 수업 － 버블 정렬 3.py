N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def find():
    global A

    if A == B:
        return 1

    for n in range(N - 1, -1, -1):
        if B[n] != n + 1:
            for i in range(n):
                if A[i] > A[i + 1]:
                    A[i], A[i + 1] = A[i + 1], A[i]

                if A == B:
                    return 1
        else:
            idx = A.index(n + 1)
            A = A[:idx] + A[idx + 1:]
            A.insert(n, n + 1)
            if A == B:
                return 1

    return 0

print(find())