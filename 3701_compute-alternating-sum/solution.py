class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summ = 0
        for num,i in enumerate(nums):
                            
            if num % 2 ==1:
                summ-=i
            else:
                summ+=i
        return summ