class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        l = 0
        r = (rows*columns) - 1

        while l <= r:
            m = (l+r) // 2

            m_row = m // columns
            m_column = m % columns
            if matrix[m_row][m_column] != target:
                if matrix[m_row][m_column] > target:
                    r = m - 1

                else:
                    l = m + 1
            else:
                return True
        
        return False


        