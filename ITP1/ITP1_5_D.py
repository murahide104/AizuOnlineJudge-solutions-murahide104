n = int(input())
l = []

for i in range(1, n+1):
    if 3 <= i and i % 3 == 0:
        l.append(i)
    elif "3" in str(i):
        l.append(i)
        
print(*l)