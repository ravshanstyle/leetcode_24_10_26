class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        other = [i for i in reversed(nums)]
        return nums+other