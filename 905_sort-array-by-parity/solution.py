class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        clean = list(filter(lambda x : x%2==0, nums))
        cl = list(filter(lambda x : x%2!=0, nums))
        return clean+cl