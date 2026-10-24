class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        target = []
        for i, j in zip(nums,index):
            target[j:j] = [i]
        return target