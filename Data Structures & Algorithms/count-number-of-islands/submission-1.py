class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0]) 

        def dfs(i, j):
            if (i == rows 
                    or i < 0
                    or j == columns
                    or j < 0
                    or grid[i][j] == "0"):
                return
            
            grid[i][j] = "0"

            dfs(i, j+1)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i-1, j)
            

        n_islands = 0

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1":
                    dfs(i,j)
                    n_islands += 1
        return n_islands
        
        
        