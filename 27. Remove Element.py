#The idea of this solution is to get the number of elements to be removed,
#Look out for edge case where the there is no element to be removed
#Replace all elements to be removed before k with those (not to be removed) after k
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        
        for i in range(len(nums)):
            if nums[i]==val:
                k-=1
        if k == len(nums):
            return k
        i=0
        while i<=k:
            print(nums)
            if nums[i]==val:
                for j in range(k,len(nums)):
                    if nums[j] != val:
                        nums[i],nums[j]=nums[j],nums[i]
                        break
            i+=1
        return k