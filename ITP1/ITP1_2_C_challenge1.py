l = [int(input()) for _ in range(6)]
l4 = l[:4]; l4.sort()
l2 = l[4:]; l2.sort()

print(sum(l4[1:]) + l2[-1])