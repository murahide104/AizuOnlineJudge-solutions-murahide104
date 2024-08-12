n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

# p=1(ユークリッド距離)
d = 0
for i in range(n):
    d += abs(x[i] - y[i])
print(d)

# p=2, p=3
for p in [2, 3]:
    d = 0
    for i in range(n):
        d += abs(x[i]-y[i])**p
    d **= (1/p)
    print(d)

# p=∞(チェビシェフ距離)
d = 0
for i in range(n):
    d = max(d, abs(x[i] - y[i]))
print(d)