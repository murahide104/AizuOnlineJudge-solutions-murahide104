n = int(input())
while True:
    op = input()
    if op == "=":
        print(n); break
    
    n2 = int(input())
    
    if op == "+":
        n += n2
    elif op == "-":
        n -= n2
    elif op == "*":
        n *= n2
    else:
        n = int(n / n2)