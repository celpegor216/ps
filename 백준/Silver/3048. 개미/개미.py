N1, N2 = map(int, input().split())
A = input()
B = input()
T = int(input())

# A와 B를 일렬로 나열, 이때 A는 주어진 문자열의 역순으로 나열해야 함에 주의
# 음수는 A의 인덱스, 양수는 B의 인덱스
lst = [x for x in range(-1, -N1 - 1, -1)] + [x for x in range(1, N2 + 1)]

for _ in range(T):
    idx = 0
    while idx < N1 + N2 - 1:
        # 전체를 나열한 lst에서 idx 위치에 있는 개미와 그 앞에 있는 개미가 다른 방향으로 움직일 경우,
        # 값이 0이 아니면서 음수와 양수 혹은 양수와 음수이므로 둘을 곱했을 때 0보다 작음
        # > 현재 인덱스가 음수일 때에만 이동해야 함
        if lst[idx] < 0 and lst[idx + 1] > 0:
            # 둘의 자리를 바꿔주고, 다다음 인덱스부터 확인함
            lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
            idx += 2
        else:
            # 그렇지 않다면 다음 인덱스부터 확인함
            idx += 1

for i in range(N1 + N2):
    if lst[i] < 0:
        print(A[lst[i]], end='')
    else:
        print(B[lst[i] - 1], end='')