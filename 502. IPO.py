#This problem is an introduction to a very rare pattern which is double heap
#We would use two heaps one for the max profits and one for the min capital
#The rest is cake
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfits = []
        minCosts = [(c,p) for c,p in zip(capital,profits)]
        heapify(minCosts)
        for i in range(k):
            while minCosts and minCosts[0][0]<=w:
                c,p = heapq.heappop(minCosts)
                heapq.heappush(maxProfits, -1*p) #We multiply by -1 because heaps in python are in ascending order by default
            if not(maxProfits): #In case we can not afford K projects
                break
            w+= -1*heapq.heappop(maxProfits)
        return w
