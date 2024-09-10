T = int(input())

for _ in range(T):
    S = input()
    N = len(S)

    bucket = [0] * 26
    idx = 0
    result = 'OK'
    while idx < N:
        char = ord(S[idx]) - ord('A')
        bucket[char] += 1

        if bucket[char] == 3:
            idx += 1

            if idx < N and S[idx] == S[idx - 1]:
                bucket[char] = 0
            else:
                result = 'FAKE'
                break
        idx += 1

    print(result)