def solution(dartResult):
    type_string = {'S': 1, 'D': 2, 'T': 3}
    
    nums = []
    types = []
    rest = ['-'] * 3
    
    idx = 0
    while idx < len(dartResult):
        if '0' <= dartResult[idx] <= '9':
            if dartResult[idx + 1] == '0':
                nums.append(10)
                idx += 2
            else:
                nums.append(int(dartResult[idx]))
                idx += 1
        elif dartResult[idx] in type_string.keys():
            types.append(dartResult[idx])
            idx += 1
        else:
            rest[len(nums) - 1] = dartResult[idx]
            idx += 1
    
    for i in range(3):
        nums[i] = nums[i] ** type_string[types[i]]
    
    for i in range(3):
        if rest[i] == '*':
            if i > 0:
                nums[i-1] *= 2
            nums[i] *= 2
        elif rest[i] == '#':
            nums[i] *= -1
    
    return sum(nums)