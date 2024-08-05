n = int(input())
for i in range(n):
    x, y, b, p = map(int, input().split())
    if 5 <= b and 2 <= p:
        print(int((x * b + y * p) * 0.8))
    else:
        price1 = x * b + y * p
        
        if b < 5 and 2 <= p:
            price2 = (x * 5 + y * p) * 0.8
        elif 5 <= b and p < 2:
            price2 = (x * b + y * 2) * 0.8
        else:
            price2 = (x * 5 + y * 2) * 0.8
        
        print(int(min(price1, price2)))