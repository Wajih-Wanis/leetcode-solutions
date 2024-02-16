import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        rows, columns = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def dfs(row,col):
            queue = collections.deque()
            queue.append((row,col))
            visited.add((row,col))
            directions = [[0,1],[0, -1],[1,0],[-1,0]]
            while queue:
                row,col = queue.popleft()
                for dr , dc in directions:
                    r = dr + row
                    c = dc + col
                    if r in range(rows) and c in range(columns) and not((r,c) in visited) and grid[r][c] == "1":
                        visited.add((r,c))
                        queue.append((r,c))
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] ==  "1" and not((r,c) in visited):
                    dfs(r,c)
                    islands+=1
        return islands