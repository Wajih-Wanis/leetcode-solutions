#The idea behind the solution is to do binary search on indices. 
#First let's get rid of the edge cases where the size is 1 and the edge case where the peak is at the start or the end
#Now we would recursively look into the array. If we find a peak then return 
#If no peak is found we would like left and right of the current element while at the same time passing last index into the function because we have to return the index at the end.
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        elif  nums[0] > nums[1]:
            return 0
        elif  nums[-1] > nums[-2]:
            return len(nums)-1

        def lookUp(array,addition):
            cur = len(array)//2
            if array[cur-1]<array[cur] and array[cur+1]<array[cur]:
                return cur + addition
            elif array[cur-1]>array[cur]:
                return lookUp(array[:cur+1],addition)
            elif array[cur+1]>array[cur]:
                return lookUp(array[cur:],addition+cur)
        return lookUp(nums,0)



