s = int(input())

h = s // (60 * 60)
m = s % (60 * 60) // 60
s = s % (60 * 60) % 60

print(f"{h}:{m}:{s}")
