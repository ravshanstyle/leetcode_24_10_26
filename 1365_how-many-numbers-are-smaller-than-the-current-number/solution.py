class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst = []
        for j in range(len(nums)):
            count = 0
            for num in nums:
                if num < nums[j]:
                    count += 1
            lst.append(count)
        return lst

        