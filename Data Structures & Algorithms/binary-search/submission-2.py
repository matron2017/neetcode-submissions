class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        r = n
        l = 0
        m = (l + r) // 2
        # go through with paper when solving next time
        #, need very good intuition with this
        # solve at leats 3 next exercise sessions in a row.
        while r >= l:
            middle = nums[m]
            if target != middle:
                if target > middle:
                    l = m + 1   
                    m = (l + r) // 2
                else:
                    r = m - 1
                    m = (l + r) // 2 
            else:
                return m

        return -1