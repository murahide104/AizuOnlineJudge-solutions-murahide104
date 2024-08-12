import math

while True:
    n = int(input())
    if n == 0: break
    l = list(map(int, input().split()))
    mean = sum(l) / n
    var = 0
    for value in l:
        var += (value - mean) ** 2 / n
    std = math.sqrt(var)
    print(std)