r, c = map(int, input().split())
l = [[0 for i in range(c+1)] for j in range(r+1)]
input_l = [list(map(int, input().split())) for _ in range(r)]

for i in range(r):
    for j in range(c):
        l[i][j] = input_l[i][j]

for i in range(r):
    for j in range(c):
        l[i][c] += l[i][j]
        l[r][j] += l[i][j]

l[r][c] = sum(l[r])

for row in l:
    print(*row)