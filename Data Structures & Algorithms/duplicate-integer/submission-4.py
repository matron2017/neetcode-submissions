class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        past = set()

        for index, item in enumerate(nums):
            if item in past:
                return True
            past.add(item)
        
        return False