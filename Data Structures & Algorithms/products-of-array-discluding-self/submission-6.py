class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        prefix = suffix = 1

        for i in range(n):
            j = -i - 1
            ans[i] *= prefix
            prefix *= nums[i]

            ans[j] *= suffix
            suffix *= nums[j]
        
        return ans