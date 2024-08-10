s = input()

for ch in s:
    if ch.isalpha():
        if ch.isupper():
            print(ch.lower(), end="")
        else:
            print(ch.upper(), end="")
    else:
        print(ch, end="")
else:
    print()

# s = input()
# print(s.swapcase())