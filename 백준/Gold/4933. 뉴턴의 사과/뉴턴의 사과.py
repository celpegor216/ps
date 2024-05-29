T = int(input())

def post_order(lst, root, dic):
    cnt = 0

    right = root - 1
    if lst[right] != 'nil':
        dic[lst[right]] = dict()
        cnt += post_order(lst, right, dic[lst[right]])
    else:
        cnt += 1

    left = right - cnt
    if lst[left] != 'nil':
        dic[lst[left]] = dict()
        cnt += post_order(lst, left, dic[lst[left]])
    else:
        cnt += 1

    return cnt + 1

for _ in range(T):
    lst_a = input().split()
    lst_b = input().split()

    dic_a = dict()
    dic_b = dict()

    if lst_a[-2] != 'nil':
        dic_a[lst_a[-2]] = dict()
        post_order(lst_a, len(lst_a) - 2, dic_a[lst_a[-2]])

    if lst_b[-2] != 'nil':
        dic_b[lst_b[-2]] = dict()
        post_order(lst_b, len(lst_b) - 2, dic_b[lst_b[-2]])

    print('true' if dic_a == dic_b else 'false')