import math
a, b, c = map(int, input().split())
rad = math.radians(c)

s = 0.5 * a * b * math.sin(rad)
l = a + b + (math.sqrt(a**2 + b**2 - 2*a*b * math.cos(rad)))
h = 2*s / a

print(s)
print(l)
print(h)