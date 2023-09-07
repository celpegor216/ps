# dp 같은데 방법을 모르겠음
# 생각했던 방법: 짝수, 홀수를 그룹화 -> 홀수 그룹 선택 제외
# ex) 주어진 수열이 [1, 2, 4, 5, 6, 7, 9, 10]일 때
# ex) 그룹화한 수열은 [0, 1, 2, 1, 1, 2, 1] (짝-홀-짝-홀-...-짝)
# ex) 여기에서 합이 K 이하가 되도록 홀수 그룹 선택하면 될 것 같은데
# ex) 홀수 그룹 선택하는 dp를 어떻게 하지?

# 투 포인터였음,,,
# 해답: https://velog.io/@harryyyyy/%EB%B0%B1%EC%A4%80-22862-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A7%9D%EC%88%98-%EC%97%B0%EC%86%8D%ED%95%9C-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4-%ED%88%AC%ED%8F%AC%EC%9D%B8%ED%84%B0-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC


N, K = map(int, input().split())
lst = list(map(int, input().split()))

end = 0
result = 0
now_even = 0
now_odd = 0

for start in range(N):
    while (now_odd <= K and end < N):
        if lst[end] % 2:
            now_odd += 1
        else:
            now_even += 1
        end += 1

        if start == 0 and end == N:
            result = now_even
            break
    
    if now_odd == K + 1:
        result = max(result, now_even)
    
    # start를 한 칸 뒤로 뺌
    if lst[start] % 2:
        now_odd -= 1
    else:
        now_even -= 1

print(result)
