import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(input()) for _ in range(N)] # 원소들
D = [int(input()) for _ in range(M)] # 찾으려는 값들

A.sort()

def bs(target):
    start = 0
    end = N - 1

    while start <= end:
        middle = (start + end) // 2

        if A[middle] == target:
            if middle > 0:
                if A[middle - 1] < A[middle]:
                    return middle
                else:
                    end = middle - 1
            else:
                return middle
        elif A[middle] > target:
            end = middle - 1
        else:
            start = middle + 1

    return -1

for d in D:
    print(bs(d))