def solution(numbers, hand):
    answer = ''
    
    left_now = [3, 0]
    right_now = [3, 2]
    
    left = [1, 4, 7]
    right = [3, 6, 9]
    
    for number in numbers:
        if number in left:
            number -= 1
            left_now = [number // 3, number % 3]
            answer += 'L'
        elif number in right:
            number -= 1
            right_now = [number // 3, number % 3]
            answer += 'R'
        else:
            if number != 0:
                number -= 1
                num = [number // 3, number % 3]
            else:
                num = [3, 1]
            from_left = abs(num[0] - left_now[0]) + abs(num[1] - left_now[1])
            from_right = abs(num[0] - right_now[0]) + abs(num[1] - right_now[1])
    
            if from_left < from_right:
                left_now = num
                answer += 'L'
            elif from_left > from_right:
                right_now = num
                answer += 'R'
            else:
                if hand == 'left':
                    left_now = num
                    answer += 'L'
                else:
                    right_now = num
                    answer += 'R'

    return answer