class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in past:
                return [past[diff], index]
            past[num] = index
        