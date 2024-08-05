a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
answer = 0

if a < 0: #凍った肉
    answer += abs(a) * c + d
    answer += b * e
else: #凍ってない肉
    answer += (b - a) * e

print(answer)