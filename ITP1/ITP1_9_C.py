n = int(input())
t_point = 0
h_point = 0

for i in range(n):
    t, h = input().split()
    if t < h:
        h_point += 3
    elif t > h:
        t_point += 3
    else:
        t_point += 1; h_point += 1

print(t_point, h_point)