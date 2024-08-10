trump = [[i for i in range(1, 14)] for j in range(4)]

n = int(input())
# 持っているカードを削除
for i in range(n):
    m, trump_num = input().split()
    trump_num = int(trump_num)
    
    if m == "S":
        trump[0].remove(trump_num)
    elif m == "H":
        trump[1].remove(trump_num)
    elif m == "C":
        trump[2].remove(trump_num)
    elif m == "D":
        trump[3].remove(trump_num)

#持っていないカードを表示
for i in range(4):
    for j in range(len(trump[i])):
        if i == 0:
            print("S", trump[i][j])
        elif i == 1:
            print("H", trump[i][j])
        elif i == 2:
            print("C", trump[i][j])
        elif i == 3:
            print("D", trump[i][j])