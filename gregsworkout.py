n = int(input())
lst = list(map(int, input().split()))

ch = 0
bi = 0
b = 0


for i in range(n):
    if i % 3 == 0:
       ch += lst[i]
    elif i % 3 == 1:
        bi += lst[i]
    else:
        b += lst[i]


m = max(ch, bi, b)
if m == ch:
    print("chest")
elif m == bi:
    print("biceps")
else:
    print("back")