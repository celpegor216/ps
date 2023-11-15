# 틀렸는데 반례들은 다 맞음... 어디서 틀린 거지?
# 해답: https://velog.io/@dasd412/%EB%B0%B1%EC%A4%80-11509-%ED%92%8D%EC%84%A0-%EB%A7%9E%EC%B6%94%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

N = int(input())
lst = list(map(int, input().split()))

cnt = [0] * 1000001

for h in lst:
    if cnt[h]:
        cnt[h] -= 1
    cnt[h - 1] += 1

print(sum(cnt))