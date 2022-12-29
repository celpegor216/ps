N = int(input())

tree = dict()
for n in range(N):
    parent, left, right = input().split()
    tree.update({parent: (left, right)})

result_pre = ''
result_mid = ''
result_post = ''

def pre(now):
    global result_pre

    if now != '.':
        result_pre += now
        pre(tree[now][0])
        pre(tree[now][1])

def mid(now):
    global result_mid

    if now != '.':
        mid(tree[now][0])
        result_mid += now
        mid(tree[now][1])

def post(now):
    global result_post

    if now != '.':
        post(tree[now][0])
        post(tree[now][1])
        result_post += now

pre('A')
mid('A')
post('A')

print(result_pre)
print(result_mid)
print(result_post)