n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = []
for i in range(m):
    b.append(int(input()))

c = [0]*n
for i in range(n):
    for j in range(m):
        c[i] += a[i][j] * b[j]

for i in range(n):
    print(c[i])