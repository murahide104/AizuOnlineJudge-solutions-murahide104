str = input()
q = int(input())
for i in range(q):
    l = list(input().split())
    l[1], l[2] = int(l[1]), int(l[2])
    if l[0] == "print":
        print(str[l[1]:l[2]+1])
    elif l[0] == "reverse":
        str = str[:l[1]] + str[l[1]:l[2]+1][::-1] + str[l[2]+1:]
    elif l[0] == "replace":
        str = str[:l[1]] + l[3] + str[l[2]+1:]