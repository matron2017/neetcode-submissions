class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        temp = []
        def backtrack(n):
            if n == len(nums):
                subsets.append(temp[:]) 
                return

            backtrack(n+1)
            temp.append(nums[n])
            backtrack(n+1)        
            temp.pop()                       

        backtrack(0)

        return subsets