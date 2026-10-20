class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        rows = len(matrix)
        columns = len(matrix[0])
        r = (rows*columns) - 1
        m = (l+r) // 2

        while r >= l:
            row = m // columns
            column = m % columns
            mid = matrix[row][column]
            if mid != target:
                if target > mid:
                    l = m + 1
                    m = (l+r) // 2
                else:
                    r = m - 1
                    m = (l+r) // 2
            else:
                return True

        return False 