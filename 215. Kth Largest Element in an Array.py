#Simply sort the array and return the len(nums)-k element
class Solution:
    def findKthLarges(self,nums: List[int], k:int) -> int:
        nums.sort()
        return nums[len(nums)-k]
