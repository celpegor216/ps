# 해답: https://comdolidol-i.tistory.com/325

N = int(input())
S = [input() for _ in range(N)]

result = ''

cnt = 0
start, end = 0, N - 1

while start <= end:
    if S[start] < S[end]:
        result += S[start]
        start += 1
    elif S[start] > S[end]:
        result += S[end]
        end -= 1
    else:
        s, e = start + 1, end - 1
        while s <= e:
            if S[s] < S[e]:
                result += S[start]
                start += 1
                break
            elif S[s] > S[e]:
                result += S[end]
                end -= 1
                break
            else:
                s += 1
                e -= 1
        else:
            result += S[start]
            start += 1  

    cnt += 1
    if not cnt % 80:
        result += '\n'

print(result)