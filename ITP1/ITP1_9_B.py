while True:
    card = input()
    if card == "-": break
    m = int(input())
    
    for i in range(m):
        h = int(input())
        card = card[h:] + card[:h]
    print(card)