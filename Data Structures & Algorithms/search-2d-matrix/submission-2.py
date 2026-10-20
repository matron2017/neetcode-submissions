class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        n = len(matrix)
        r = n - 1
        m = (l+r) // 2
        correct_row = []
        while l <= r:
            #to check if current row, chekc l and r
            #
            mid_row = matrix[m]
            if mid_row[0] > target or mid_row[-1] < target:
                if target > mid_row[-1]:
                    l = m + 1
                    m = (l+r) // 2
                else: #else would mean target < mid_row[0]
                    r = m - 1
                    m = (l+r) // 2

            else:
                correct_row = mid_row
                break
        
        if correct_row == []:
            return False

        #checking the row with binary search is easy,
        # but how to get the rown in O(log n) compelxiti instead of O(n)?
        #. Do binary search on row also?

        l = 0
        n_row = len(correct_row)
        r = n_row - 1
        m = (l+r) // 2
        while l <= r:
            mid = correct_row[m]
            if target != mid:
                if target > mid:
                    l = m + 1
                    m = (l+r) // 2
                else:
                    r = m - 1
                    m = (l+r) // 2
            else:
                return True
        
        return False


