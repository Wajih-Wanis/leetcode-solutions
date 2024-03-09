#The idea of this solution is to replace replace at each iteration the slot with the minium of its two bases. Thus we get the minium at the peak of the triangleclass Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return None
        
        height = len(triangle)-1

        while height > 0:
            height -=1
            temp = triangle[height+1]
            print(temp)
            for i in range(len(triangle[height])):
                triangle[height][i]=min(triangle[height][i]+temp[i],triangle[height][i]+temp[i+1])
        
        return triangle[0][0]
