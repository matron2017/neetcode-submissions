class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        n = len(nums)
        ans = [0] * n

        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for j in range(n-1, -1, -1):
            ans[j] *= postfix
            postfix *= nums[j]
        
        return ans