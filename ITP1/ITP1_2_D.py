w, h, x, y, r = map(int, input().split())

if 0 <= x-r and x+r <= w and 0 <= y-r and y+r <= h:
    print("Yes")
else:
    print("No")