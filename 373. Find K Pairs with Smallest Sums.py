#The solution is to simply make a heap with its key being the sum,
#Fix the heap size at K to save space 
#Break the loop if no added value to save time
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        summer = []
        heapify(summer)
        for d in nums1:
            for n in nums2:
                if len(summer)<k:
                    heapq.heappush(summer,((-(d+n),[d,n])))
                else:
                    som,l = heapq.heappop(summer)
                    if -(d+n) > som:
                        heapq.heappush(summer,(-(d+n),[d,n]))
                    else:
                        heapq.heappush(summer,(som,l))
                        break
        while len(result)<k:
            result.append(heapq.heappop(summer)[1])
        return result
