while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    
    l = [[] for _ in range(h)]
    for i in range(1, h+1):
        for j in range(1, w+1):
            if (i + j) % 2 == 0:
                l[i-1].append("#")
            else:
                l[i-1].append(".")
    
    for sublist in l:
        print("".join(sublist))
    else:
        print("")