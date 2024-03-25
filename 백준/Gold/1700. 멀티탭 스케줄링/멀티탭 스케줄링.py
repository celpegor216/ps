# 힌트: 그리디
# 해답: https://magentino.tistory.com/88

N, K = map(int, input().split())
lst = list(map(int, input().split()))

now = set()
cnt = 0

for k in range(K):
    now.add(lst[k])

    if len(now) > N:
        cnt += 1

        target = 0
        target_next_idx = 0
        for item in now:
            try:
                item_next_idx = lst[k:].index(item)
            except:
                item_next_idx = K
            
            if item_next_idx > target_next_idx:
                target = item
                target_next_idx = item_next_idx
        
        now.remove(target)

print(cnt)