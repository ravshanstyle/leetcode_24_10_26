n = int(input())
m = 0
p = 0
for _ in range(n):
    a, b = map(int, input().split())
    p += (b-a)
    if p > m:
        m = p
print(m)