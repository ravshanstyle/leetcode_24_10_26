a = input()
count = 0
prev = 0
res = ""
max = 0
#1000000001
for i in range(len(a)):

    if a[prev] == a[i]:
        count += 1
    else:
        if max < count:
            max = count
        count = 0
        prev = i

if max >= 7:
    res = "YES"
else:
    res ="NO"
print(res)
