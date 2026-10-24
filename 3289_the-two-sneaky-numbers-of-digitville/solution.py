class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        seen = set()
        res = []
        for num in nums:
            if num in seen:
                res.append(num)
                if len(res) == 2:
                    return res
            seen.add(num)
        return res