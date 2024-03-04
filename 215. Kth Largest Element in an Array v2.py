#In this solution we would heapify the list, and then pop elements and increment k. Until we get to the kth element and then return it. 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        kth = len(nums)
        while nums:
            if k==kth:
                return heapq.heappop(nums)
            heapq.heappop(nums)
            k+=1
            if k==kth:
                return heapq.heappop(nums)
        return heapq.heappop(nums)
