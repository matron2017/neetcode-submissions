class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefix = 1
        # nums = 1 [1, 2, 3, 4] 1
        # res = [0, 0, 0, 0] 
        for i in range(n):
            
            res[i] = prefix
            prefix *= nums[i]
            # res = [1, 1, 2, 6]

        suffix = 1
        for j in range(n - 1, -1, -1):
            
            res[j] *= suffix
            suffix *= nums[j]

        return res