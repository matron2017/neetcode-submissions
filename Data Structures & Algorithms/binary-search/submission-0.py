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
                    # jos midd in 2 ja top 4 niin 4 + 2 // 3,  jos mid 1 ja top 4, 1 + 4 // 2 = 2
                    # 1 3,   1 + 3 // 2,  2,     
                    m = (l + r) // 2
                else:
                    r = m - 1
                    m = (l + r) // 2 
            # 1 2 3, 
            else:
                return m

        return -1