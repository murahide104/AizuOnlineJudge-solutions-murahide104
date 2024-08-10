while True:
    n = int(input())
    if n == 0: break
    l = [int(x) for x in input().split()]
    l.sort()
    
    answer = 1000000
    for i in range(len(l)-1):
        if abs(l[i] - l[i+1]) < answer:
            answer = abs(l[i] - l[i+1])
    
    print(answer)