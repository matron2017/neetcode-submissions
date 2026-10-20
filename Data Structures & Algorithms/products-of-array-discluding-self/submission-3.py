class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = 1
        # nums = 1 [1, 2, 3, 4] 1
        # res = [1, 1, 1, 1] 
        suffix = 1
        for i in range(n):
            j = -i - 1
            res[i] *= prefix
            prefix *= nums[i]
            res[j] *= suffix
            suffix *= nums[j]

        return res