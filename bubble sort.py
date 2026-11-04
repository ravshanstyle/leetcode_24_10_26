def bubblesort(n):
    a = len(n)
    for i in range(a):
        for j in range(a-i-1):
            if n[j] > n[j+1]:
                n[j],n[j+1] = n[j+1],n[j]
                
    return n
print(bubblesort([7, 12, 9, 11, 3]))
