n = input()
res = "YES"
count = 0
for i in range(len(n)):
    if n[i] == '4' or n[i] == '7':
        count += 1
if count != 4 and count != 7:
    res = "NO"
print(res)
