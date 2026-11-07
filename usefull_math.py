s = input()
lst = []
for i in range(len(s)):
    if s[i].isdigit():
        lst.append(s[i])
lst.sort()
print("+".join(lst))
