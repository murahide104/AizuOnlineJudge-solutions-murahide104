n = int(input())
m = int(input())
max_m = 0

for i in range(n):
    in_car, out_car = map(int, input().split())
    m += in_car; m -= out_car
    if m < 0:
        print(0); break
    if max_m < m:
        max_m = m
else:
    print(max_m)