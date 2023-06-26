a, b, c, d, e, f = map(int, input().split())

x = (f * b - e * c) // (b * d - a * e)
y = (f * a - c * d) // (e * a - b * d)

print(x, y)