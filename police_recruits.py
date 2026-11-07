n = int(input())
lst = list(map(int,input().split()))
police = 0

c_gone = 0

for i in range(n):
    if lst[i] > 0:
        police += lst[i]
    elif lst[i] == -1:
        if police <= 0:
            c_gone += 1
        else:
            police -= 1
print(c_gone)