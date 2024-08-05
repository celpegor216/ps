N = int(input())
dic = dict()

def pre_order(now):
    if now == '.':
        return ''

    if not dic.get(now):
        return now

    left = pre_order(dic[now][0])
    right = pre_order(dic[now][1])

    return now + left + right

def in_order(now):
    if now == '.':
        return ''

    if not dic.get(now):
        return now

    left = in_order(dic[now][0])
    right = in_order(dic[now][1])

    return left + now + right

def post_order(now):
    if now == '.':
        return ''

    if not dic.get(now):
        return now

    left = post_order(dic[now][0])
    right = post_order(dic[now][1])

    return left + right + now

for _ in range(N):
    now, left, right = input().split()
    dic[now] = [left, right]

print(pre_order('A'))
print(in_order('A'))
print(post_order('A'))