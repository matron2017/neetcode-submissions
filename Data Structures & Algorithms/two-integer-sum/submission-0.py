class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in past:
                return [past[diff], i]
            past[nums[i]] = i
