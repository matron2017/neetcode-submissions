class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(i, num_sum):
            if num_sum > target or i == len(nums):
                return

            if num_sum == target:
                res.append(sol[:])
                return

            sol.append(nums[i])
            backtrack(i, num_sum + nums[i])
            sol.pop()
            

            backtrack(i+1, num_sum)

        backtrack(0, 0)
        return res
