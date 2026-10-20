class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return

            # Don't include nums[i] (here i=1 and sol = [2])
            backtrack(i+1)

            # now INlucde nums[i] # i=1 nums[1] = 2
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        # res = [[], [3], [2], [2,3]]
        backtrack(0)
        return res

