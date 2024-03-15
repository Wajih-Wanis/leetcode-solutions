#We will simply check if an element is already visited, if not keep it. If visited we will look for the next non visited element and swap them
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited = set()
        i=0
        while i<len(nums):
            if nums[i] not in visited:
                visited.add(nums[i])
                i+=1
            else:
                mem=i
                while nums[i] in visited:
                    i+=1
                    if i == len(nums):
                        return len(visited)
                visited.add(nums[i])
                nums[i],nums[mem]=nums[mem],nums[i]
                i = mem+1
        return len(visited)