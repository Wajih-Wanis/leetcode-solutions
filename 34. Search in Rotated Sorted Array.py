#The first intuition is that if the target is smaller than the first element and greater than the last element it means that it does not exist in the table
#Then we would perform simple double pointer search. 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0] and target > nums[-1]:
            return -1
        i=0
        j= len(nums)-1
        while i<j:
            if nums[i]==target:
                return i
            elif nums[j]==target:
                return j
            else:
                i+=1
                j-=1
        return i if nums[i]==target else -1
