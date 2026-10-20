class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            #Explore all combinations WITHOUT nums[i] (i=0, 1)
            backtrack(i+1)
            
            #Explroe all combinaitons WITH nums[i] (1)
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)

        return res


