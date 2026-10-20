class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        l = 0
        t = rows*columns   # 12
        r = t - 1 # 11 etc.
        m = (l+r) // 2 # 5
        while r >= l:
            i = m // columns  # 5 // 4 = 1  row index
            j = m % columns   # 5 % 4 = 1 column index
            mid = matrix[i][j]
            if target != mid:
                if target > mid:
                    l = m + 1
                    m = (l+r) //  2

            
                else:
                    r = m - 1
                    m = (l+r) // 2

            else: 
                return True

        return False



