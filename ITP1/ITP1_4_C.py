while True:
    a, op, b = input().split()
    
    if op == "?":
        break
    a, b = int(a), int(b)
    
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    else:
        print(int(a / b))