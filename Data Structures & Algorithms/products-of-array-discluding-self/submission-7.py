class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        prefix = postfix = 1

        for i in range(n):
            j = -i - 1
            ans[i] = prefix
            prefix *= nums[i]

        for j in range(n-1, -1, -1):

            ans[j] *= postfix
            postfix *= nums[j]
 
        
        return ans