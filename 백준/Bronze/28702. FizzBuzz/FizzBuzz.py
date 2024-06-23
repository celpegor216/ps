numbers = [0] * 3

result = 0
for i in range(3):
    s = input()

    try:
        numbers[i] = int(s)

        if not result:
            num = numbers[i] + 3 - i
            
            if not num % 3 and not num % 5:
                result = 'FizzBuzz'
            elif not num % 3:
                result = 'Fizz'
            elif not num % 5:
                result = 'Buzz'
            else:
                result = str(num)
    except:
        numbers[i] = 0

print(result)