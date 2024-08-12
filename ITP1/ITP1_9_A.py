w = input().upper()
count = 0

while True:
    t = input().split()
    if "END_OF_TEXT" in t: break
    t = [word.upper() for word in t]
    count += t.count(w)

print(count)