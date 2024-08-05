D, L = map(int, input().split())
count = 0

count += D // L
count += D % L

print(count)
