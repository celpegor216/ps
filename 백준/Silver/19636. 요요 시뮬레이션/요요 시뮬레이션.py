# 체중, 다이어트 전 에너지 섭취량, 기초 대사량 변화 역치
weight, before_plus, T = map(int, input().split())
consume = before_plus    # 기초 대사량은 에너지 섭취량과 같음

# 다이어트 기간, 다이어트 에너지 섭취량, 다이어트 활동 대사량
duration, plus, minus = map(int, input().split())

# 체중은 (일일 에너지 섭취량 − 일일 에너지 소비량)만큼 더해진다

# 첫 번째 줄에는 일일 기초 대사량의 변화를 고려하지 않았을 때의 다이어트 후 예상 체중과 일일 기초 대사량을 출력
if weight + ((plus - minus - consume) * duration) > 0:
    print(weight + ((plus - minus - consume) * duration), consume)
else:
    # 다이어트 도중 데시의 사망이 예상되는 경우 Danger Diet를 출력
    print('Danger Diet')

# 두 번째 줄에는 일일 기초 대사량의 변화를 고려했을 때의 다이어트 후 예상 체중과 일일 기초 대사량, 요요 현상 발생 여부 출력
# 변화한 일일 기초 대사량을 가지고 다이어트 전 일일 에너지 섭취량과 다이어트 전 일일 활동 대사량으로 돌아갔을 때 체중이 증가하는 요요 현상이 발생하는 경우 YOYO, 발생하지 않는 경우 NO
tmp_weight = weight
tmp_consume = consume
for _ in range(duration):
    tmp_weight += (plus - minus - tmp_consume)

    if abs(plus - minus - tmp_consume) > T:
        tmp_consume += (plus - minus - tmp_consume) // 2

    if tmp_weight <= 0 or tmp_consume <= 0:
        print('Danger Diet')
        break
else:
    if before_plus - tmp_consume > 0:
        print(tmp_weight, tmp_consume, 'YOYO')
    else:
        print(tmp_weight, tmp_consume, 'NO')