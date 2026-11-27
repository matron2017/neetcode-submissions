class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if nums[0] < nums[-1]:
            r = 0
        else:
            n = len(nums)
            l = 0
            r = n - 1
            while l < r:
                m = (l+r) // 2
                
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m

        min_i = r
        if min_i == 0:
            l = 0
            r = n - 1
        elif nums[0] <= target <= nums[min_i-1]:
            l = 0
            r = min_i - 1
        else :
            l = min_i
            r = n - 1

        while l <= r:
            m = (l+r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        return -1
