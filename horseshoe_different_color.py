lst = list(map(int,input().split()))
lst.sort()
count = 0
for i in range(1, 4):
    if lst[i] == lst[i - 1]:
        count += 1
print(count)
