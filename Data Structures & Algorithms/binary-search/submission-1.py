class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        r = n
        l = 0
        m = (l + r) // 2
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