class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        kopaytma = 1
        summa = 0
        while n != 0:
            qoldiq = n % 10
            print(qoldiq)
            kopaytma *= qoldiq
            summa += qoldiq
            n = n//10
            
        return kopaytma-summa