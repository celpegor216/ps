N = int(input())

end_zero = 0
end_one = 1

for n in range(1, N):
    temp_zero = end_zero + end_one
    temp_one = end_zero
    
    end_zero = temp_zero
    end_one = temp_one

print(end_zero + end_one)