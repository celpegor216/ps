lst = [input() for _ in range(5)]

nums = {'**** ** ** ****': 0, '  *  *  *  *  *': 1, 
        '***  *****  ***': 2, '***  ****  ****': 3,
        '* ** ****  *  *': 4, '****  ***  ****': 5,
        '****  **** ****': 6, '***  *  *  *  *': 7,
        '**** ***** ****': 8, '**** ****  ****': 9}

code = 0

for i in range(0, len(lst[0]), 4):
    num = ''
    for j in range(5):
        num += lst[j][i:i+3]
    
    if num in nums:
        code = code * 10 + nums[num]
    else:
        code = -1
        break

if code == -1 or code % 6:
    print("BOOM!!")
else:
    print("BEER!!")