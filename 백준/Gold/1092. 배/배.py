# 힌트: 그리디, 정렬
# 해답: https://yuna0125.tistory.com/49

N = int(input())
cranes = sorted(map(int, input().split()), reverse=True)
M = int(input())
boxes = sorted(map(int, input().split()), reverse=True)

if cranes[0] < boxes[0]:
    print(-1)
else:
    result = 0

    while boxes:
        for crane in cranes:
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
        
        result += 1
    
    print(result)