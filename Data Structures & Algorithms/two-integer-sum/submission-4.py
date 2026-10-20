class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past = {}

        for index, num in enumerate(nums):
            curr = target - num
            if curr in past:
                return [past[curr], index]
            
            past[num] = index
        