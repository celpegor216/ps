# 시간초과 해결 못 함
# 해답: https://bba-dda.tistory.com/95

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
dic = dict()
keys = []

def findIdx(num):
    start, end = 0, len(keys) - 1
    result = end

    while start <= end:
        middle = (start + end) // 2

        if keys[middle] >= num:
            result = middle
            end = middle - 1
        else:
            start = middle + 1

    return result

for n in range(N):
    k, v = map(int, input().split())
    dic[k] = v
    keys.insert(findIdx(k), k)

def findKey(num):
    idx = findIdx(num)

    left = abs(num - keys[idx - 1])
    right = abs(num - keys[idx])

    if left == right :
        return -2
    else:
        mink = min(left, right)
        if mink > K:
            return - 1
        elif mink == left:
            return keys[idx - 1]
        elif mink == right:
            return keys[idx]

answers = []

for m in range(M):
    tmp = list(map(int, input().split()))

    if tmp[0] == 1:
        dic[tmp[1]] = tmp[2]
        keys.insert(findIdx(tmp[1]), tmp[1])
    elif tmp[0] == 2:
        key = findKey(tmp[1])

        if key >= 0:
            dic[key] = tmp[2]
    else:
        key = findKey(tmp[1])

        if key == -1:
            answers.append(-1)
        elif key == -2:
            answers.append('?')
        else:
            answers.append(dic[key])

for item in answers:
    print(item)