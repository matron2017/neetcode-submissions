class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        prefix = 1

        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n):
            j = -i - 1
            ans[j] *= postfix
            postfix *= nums[j]
        
        return ans