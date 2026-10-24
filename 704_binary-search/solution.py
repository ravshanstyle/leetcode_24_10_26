class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums)-1
#[-1,0,3,5,9,12]
# ^           ^    
        mid = (right+left)//2
        while left <= right :
            mid = (right+left)//2
            if nums[mid] == target:
                return mid
                res = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1      
        return -1