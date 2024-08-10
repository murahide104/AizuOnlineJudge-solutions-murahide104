dic = {}
for i in range(26):
    dic[chr(97+i)] = 0

while True:
    try:
        s = input()
        s = s.lower()
        
        for i in s:
            if i.isalpha():
                dic[i] += 1
    except EOFError:
        break
    
for key in dic:
        print(f"{key} : {dic[key]}")