#First remove edge case of empty array
#Then double pointer through the array to find indices
#Finally check for the edge case where the result comes after i becomes less than j 
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        i=0
        j=len(nums)-1
        while i<j:
            print(f"i is {i} and j is {j}")
            if nums[i]==target:
                k=i
                while k<len(nums)-1:
                    if nums[k+1]==target:
                        k+=1
                    else:
                        break
                return [i,k]
            elif nums[j]==target:
                k=j
                while k>0:
                    if nums[k-1]==target:
                        k-=1
                    else:
                        break
                return [k,j]
            else:
                i+=1
                j-=1
        if nums[i]==target:
            return [i,i]
        if nums[j] == target:
            return [j,j]
        return [-1,-1]
