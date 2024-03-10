#The idea of this solution is to sum down, then sum to the right
#Finally sum the minimum in right and down thus getting the result in the last cell
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
            
        
        m, n = len(grid), len(grid[0])
        
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        #print(f"grid after loop 1: {grid}")
        
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        #print(f"grid after loop 2: {grid}")

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        #print(f"final grid: {grid}")
        
        return grid[-1][-1]