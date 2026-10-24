class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i,num in enumerate(nums):
            son = 0
            while num != 0:
                qol = num % 10
                son += qol
                num //= 10
            nums[i] = son
        return min(nums) 
    
        