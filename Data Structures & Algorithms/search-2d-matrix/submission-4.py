class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        rows = len(matrix)
        columns = len(matrix[0])
        n = rows * columns
        r = n - 1
        m = (l+r) // 2
        while r >=l:
            row = m // columns
            column = m % columns
            number = matrix[row][column] 
            if target != number:
                if target > number:
                    l = m + 1
                    m = (l+r) // 2
                else:
                    r = m - 1
                    m = (l+r) // 2
            else:
                return True
        return False