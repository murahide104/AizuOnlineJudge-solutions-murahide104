while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    l = list(map(int, input().split()))
    answer = 0
    for i in range(n-1):
        for j in range(1,len(l)):
            if answer < l[0] + l[j] <= m:
                answer = l[0] + l[j]
        else:
            del l[0]
    
    print(answer if answer else "NONE")
