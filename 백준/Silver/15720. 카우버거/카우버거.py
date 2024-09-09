B, C, D = map(int, input().split())
burgers = sorted(map(int, input().split()))
sides = sorted(map(int, input().split()))
drinks = sorted(map(int, input().split()))

total_original = sum(burgers) + sum(sides) + sum(drinks)
total_discount = 0

minv = min(B, C, D)
for i in range(1, minv + 1):
    total_discount += ((burgers[-i] + sides[-i] + drinks[-i]) * 9) // 10

for b in range(B - minv):
    total_discount += burgers[b]
for c in range(C - minv):
    total_discount += sides[c]
for d in range(D - minv):
    total_discount += drinks[d]

print(total_original)
print(total_discount)