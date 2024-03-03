#The intuition of this problem is to perform a simple binary search
#However since the array is rotated, we can do a little trick which goes like this
#If the first element is larger than the last element then the min is inside that portion 
#If the first element is less than the last element then the min could be the first element or in the other portion
#Eliminate the edge cases where the array is empty or have only one element 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        def miner(array):
            if len(array)==1:
                return array[0]
            mid = len(array)//2
            if array[0]>array[mid]:
                return min(array[mid],miner(array[:mid]))
            elif array[0]<array[mid]:
                return min(array[0],miner(array[mid:]))
        return miner(nums)
