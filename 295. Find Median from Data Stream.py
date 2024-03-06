#The idea of this solution is to have two heaps, a max heap and a min heap
#If the stream is odd than returning smallest element in maxHeap otherwise 
#Returns the average of it plus the greatest element in the minHeap
class MedianFinder:

    def __init__(self):
        self.maxHeap = []  
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -num) 
        heappush(self.minHeap, -self.maxHeap[0])  
        heappop(self.maxHeap)
        
        if len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -self.minHeap[0])
            heappop(self.minHeap)

    def findMedian(self) -> float:
        #print(f"maxHeap is {self.maxHeap} minHeap is {self.minHeap}")
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
