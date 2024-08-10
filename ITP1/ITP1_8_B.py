while True:
    x = input()
    if x == "0": break
    
    total = 0
    for i in x:
        total += int(i)
    
    print(total)

# print(sum([int(val) for val in input()]))