class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        n = len(nums)
        r = n - 1
        while r > l:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        def binary_search(l, r):
            m = (l+r) // 2
            while r >= l:
                number = nums[m]
                if number != target:
                    if target > number:
                        l = m + 1
                        m = (l+r) // 2
                    else:
                        r = m - 1
                        m = (l+r) // 2        
                else:
                    return m
            
            return -1

        if r == 0:
            return binary_search(0, n - 1)
        elif nums[r] <= target <= nums[n - 1]:
            return binary_search(r, n - 1)
        else:
            return binary_search(0, r - 1)
        
            