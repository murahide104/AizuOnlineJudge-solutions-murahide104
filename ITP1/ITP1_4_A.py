a, b = map(int, input().split())

d = int(a / b)
r = a % b
f = a / b

print(f"{d} {r} {f:.5f}")