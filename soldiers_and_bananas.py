cost_for_banana , amount_of_money, num_of_bananas = map(int, input().split())
borrow = 0
total = 0

# 3 6 9 12 
for i in range(1, num_of_bananas + 1):
    total += cost_for_banana * i

if borrow  > (amount_of_money - total):
    borrow = amount_of_money - total
# qarz qachonki undagi pul totaldan kam bo'lsa
print(abs(borrow)) 