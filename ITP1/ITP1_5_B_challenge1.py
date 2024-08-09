h, w, c = input().split()
h, w = int(h), int(w)

print("+" + "-"*(h-2) + "+")
for i in range(w-2):
    if i == ((w-2)//2):
        print("|" + "."*(h//2-1) + c + "."*(h//2-1) + "|")
    else:
        print("|" + "."*(h-2) + "|")
print("+" + "-"*(h-2) + "+")