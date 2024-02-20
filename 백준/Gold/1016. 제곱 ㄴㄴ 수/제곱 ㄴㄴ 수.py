# 에라토스테네스의 체는 아는데 풀이를 모르겠음
# 해답: https://imksh.com/69

minv, maxv = map(int, input().split())

used = [0] * (maxv - minv + 1)

i = 2
while i ** 2 <= maxv:
    square = i ** 2

    # remain: j가 minv 보다 같거나 크게 만들기 위한 값
    # minv가 square로 나누어 떨어지지 않는다면,
    # 발생하는 소숫점을 보정하기 위해 값을 1로 지정
    remain = 0 if not minv % square else 1

    # square * j: square로 나누어 떨어지면서 minv보다 같거나 큰 값
    j = minv // square + remain
    while square * j <= maxv:
        used[square * j - minv] = 1
        j += 1
    
    i += 1

print(len(used) - sum(used))