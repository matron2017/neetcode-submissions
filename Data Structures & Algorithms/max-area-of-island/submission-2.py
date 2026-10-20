class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        def dfs(i, j):
            if (i >= rows 
                or i < 0
                or j >= columns
                or j < 0
                or grid[i][j] == 0
            ):

                return 0
            
            grid[i][j] = 0

            return  1 + dfs(i, j+1) + dfs(i+1, j) + dfs(i, j-1) + dfs(i-1, j)    
        
        max_area = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    max_area = max(max_area, area)

        return max_area

