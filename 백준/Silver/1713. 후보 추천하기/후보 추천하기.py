# heapq 쓸 수 있을 것 같은데 추천 횟수 늘렸을 때 자동으로 재정렬 될지 모르겠음

N = int(input())
Q = int(input())
lst = list(map(int, input().split()))

frames = []

for item in lst:
    min_value = Q + 1
    min_idx = []
    length = len(frames)

    for i in range(length):
        if min_value > frames[i][1]:
            min_value = frames[i][1]
            min_idx = [i]
        elif min_value == frames[i][1]:
            min_idx.append(i)

        if frames[i][0] == item:
            frames[i][1] += 1
            break
    else:
        if length == N:
            frames.pop(min_idx[0])
        frames.append([item, 1])

print(*sorted([frame[0] for frame in frames]))