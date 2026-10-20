class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff in past:
                return [past[diff], index]
            past[value] = index
        