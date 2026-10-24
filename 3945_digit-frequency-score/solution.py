from collections import Counter

class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        summa =0
        freq = Counter(str(n))
        return sum(int(i) * j for i , j in freq.items())
            
        
       
        
       
      