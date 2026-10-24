class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        return sum((filter(lambda x : x%m!=0, range(1,n+1))))-sum((filter(lambda x : x%m==0, range(1,n+1))))