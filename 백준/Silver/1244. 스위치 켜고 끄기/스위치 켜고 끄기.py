N = int(input())
lst = list(map(int, input().split()))

for _ in range(int(input())):
    gender, num = map(int, input().split())

    idx = num - 1
    if gender == 1:
        while idx < N:
            lst[idx] = 1 if not lst[idx] else 0
            idx += num
    else:
        lst[idx] = 1 if not lst[idx] else 0
        cnt = 1
        while idx + cnt < N and idx - cnt >= 0:
            if lst[idx + cnt] != lst[idx - cnt]:
                break
            lst[idx + cnt] = 1 if not lst[idx + cnt] else 0
            lst[idx - cnt] = 1 if not lst[idx - cnt] else 0
            cnt += 1

for n in range(N):
    if n > 0 and n % 20 == 0:
        print()
    print(lst[n], end=' ')