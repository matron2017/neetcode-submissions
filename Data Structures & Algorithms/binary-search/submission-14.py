class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        n = len(nums)
        r = n - 1
        m = (l+r)//2

        while r >= l:
            number = nums[m]
            if number != target:
                if target > number:
                    l = m + 1
                    m = (l+r) // 2
                else:
                    r = m - 1
                    m = (l+r) //2
            else:
                return m

        return -1