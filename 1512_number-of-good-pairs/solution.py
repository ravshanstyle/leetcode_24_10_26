from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for num, i in Counter(nums).items():
            count += (i*(i-1))//2
        return count

