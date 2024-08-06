while True:
    n = int(input())
    if n == 0:
        break
    
    l = []
    for i in range(n):
        l.append(int(input()))
    
    l.sort()
    print(int(sum(l[1:-1]) / len(l[1:-1])))