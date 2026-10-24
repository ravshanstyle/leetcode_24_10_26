class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summa = 0
        res = []
        for i in range(len(nums)):
            summa += nums[i]
            res.append(summa)
        return res
        