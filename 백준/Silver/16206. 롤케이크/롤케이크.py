# 자를 롤케이크를 하나 고른다. 길이가 1보다 큰 롤케이크만 자를 수 있다.
# 이때, 고른 롤케이크의 길이를 x라고 한다.
# 0보다 크고, x보다 작은 자연수 y를 고른다.
# 롤케이크를 잘라 길이가 y, x-y인 롤케이크 두 개로 만든다.

# 최대 M번 자를 수 있다. 이때, 만들 수 있는 길이가 10인 롤케이크 개수의 최댓값

# 10으로 나눴을 때 나머지가 0이면서 10보다 큰 것들 부터 먼저 자르기
# 그러고 나서도 자를 수 있는 횟수가 남는다면 긴 거 하나씩 자르기

N, M = map(int, input().split())
lst = list(map(int, input().split()))

result = 0

# buckets[i]: 10으로 나눴을 때 나머지가 i이면서 10 초과인 수의 개수
buckets = [[] for _ in range(10)]
for item in lst:
    if item < 10:
        continue
    elif item == 10:
        result += 1
    else:
        buckets[item % 10].append(item)

buckets[0].sort()

def check():
    global result, M

    for bucket in buckets:
        for item in bucket:
            cnt = (item // 10)
            if not item % 10:
                cnt -= 1

            if cnt <= M:
                M -= cnt
                result += item // 10
            else:
                result += M
                M = 0

            if M == 0:
                return

check()

print(result)