class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        
        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(sol[:])
                return

            if cur_sum > target or i == n:
                return

            sol.append(nums[i])
            backtrack(i, sum(sol))
            sol.pop()

            backtrack(i+1, sum(sol))
            
        backtrack(0, 0)

        return res

